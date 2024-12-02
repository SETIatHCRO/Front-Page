import numpy as np
import pandas as pd
import toml
from astropy.coordinates import ITRS, SkyCoord, AltAz, EarthLocation
import astropy.units as u
from astropy.time import Time,TimeDelta
import os
from scipy.constants import c


import matplotlib
# make plots "pretty"
rc_params_fname = "./rc_params.py"
if os.path.exists(os.path.exists(rc_params_fname)):
    exec(open(rc_params_fname).read())
import matplotlib.pyplot as plt


def normal_dist2D(x, y, mean , sd):
    prob_density = np.exp(-0.5*( ((x-mean)/sd)**2 + ((y-mean)/sd)**2) )
    return prob_density

def parse_toml(toml_dict):
    """
    Parse a toml file as a pandas dataframe
    with columns of [x,y,z]
    """
    df = pd.DataFrame()
    df = df.from_dict(toml_dict['antennas'])[['name','position']]
    df.index = np.char.upper(list(df['name']))
    df = df.drop(columns=['name'])

    pos = np.array([i for i in df['position'].values])
    df = df.drop(columns=['position'])
    df['x'] = pos[:,0]
    df['y'] = pos[:,1]
    df['z'] = pos[:,2]
    return df

def compute_uvw(ts, source, ant_coordinates):
    """Computes UVW antenna coordinates with respect to reference

    Args:
        ts: array of Times to compute the coordinates
        source: source SkyCoord
        ant_coordinates: antenna ECEF coordinates.
             This is indexed as (antenna_number, xyz)

    Returns:
        The UVW coordinates in metres of each of the baselines formed
        between each of the antennas and the phasing reference. This
        is indexed as (time, antenna_number, uvw)
    """
    baselines_itrs = []
    for iant1 in range(len(ant_coordinates)):
        for iant2 in range(iant1, len(ant_coordinates)):
            baselines_itrs.append(ant_coordinates[iant2] -\
                    ant_coordinates[iant1])

    baselines_itrs = np.array(baselines_itrs)
    #baselines_itrs = ant_coordinates - ref_coordinates

    # Calculation of vector orthogonal to line-of-sight
    # and pointing due north.
    north_radec = [source.ra.deg, source.dec.deg + 90]
    if north_radec[1] > 90:
        north_radec[1] = 180 - north_radec[1]
        north_radec[0] = 180 + north_radec[0]
    north = SkyCoord(ra=north_radec[0]*u.deg, dec=north_radec[1]*u.deg)

    source_itrs = source.transform_to(ITRS(obstime=Time(ts))).cartesian
    north_itrs = north.transform_to(ITRS(obstime=Time(ts))).cartesian
    east_itrs = north_itrs.cross(source_itrs)

    ww = baselines_itrs @ source_itrs.xyz.value
    vv = baselines_itrs @ north_itrs.xyz.value
    uu = baselines_itrs @ east_itrs.xyz.value
    uvw = np.stack((uu.T, vv.T, ww.T), axis=-1)

    return uvw

##############################################################################
# User input #
##############

# Friday August 16, 7:15 PM PST
t_now = 1723860949 # unix time

# Calculate UVWs for 6h track, 5 mins integration
t_range = np.arange(t_now, t_now + 6*3600, 300)

# Assume pointing at 3c286
# coordinates at the time were
# az,el ~= (261.6, 59.3)
ra = 13.51896899 * 360 / 24. # deg
dec = 30.509157660           # deg

# Observing frequency, I don't assume BW, so UVW will only be at a single freq
obsfreq = 3e9 #Hz

# telinfo file
telinfo_fname = "telinfo_ata.toml"
##############################################################################

telinfo = toml.load(telinfo_fname)
itrf = parse_toml(telinfo)

source = SkyCoord(ra, dec, unit='deg')

ts = Time(t_range, format='unix')
uvws = compute_uvw(ts, source, itrf[['x', 'y', 'z']].values)

# cycle through each uvw integration
uvws = uvws.reshape(-1, uvws.shape[-1])

# UV is a hermitian matrix, so we "populate" the entire matrix by 
# mirroring wrt the origin
uv = np.concatenate((uvws[:,0], -1*uvws[:,0])), np.concatenate((uvws[:,1], -1*uvws[:,1]))
plt.scatter(uv[0], uv[1], color="black", s=3)
plt.xlabel("U [m]")
plt.ylabel("V [m]")


# Assume doing this at 3GHz
lmbd = c/obsfreq

# UV [m] -> UV[lambda]
uv /= np.array(lmbd)

# This is a bit arbitrary, should think of a better way to do this
cellsize = int(np.max((np.max(uv[0]), np.max(uv[1])))/12)

# Let's grid
hist = plt.hist2d(uv[0], uv[1], bins=cellsize)
grid = hist[0]

# This seemed to be needed for some reason (plotting?)
dd = np.flipud(grid.T)

# Increase the resolution by 12x in the image plane by padding zeros on either side of the gridded matrix
dd = np.pad(dd, cellsize*6, mode='constant', constant_values=0)

# Inverse FFT and shiftshift
f = np.fft.fftshift(np.fft.ifft2(dd))

# define the extent in UV-plane
u_extent = np.abs((hist[1][0] - hist[1][1]) * dd.shape[0])
v_extent = np.abs((hist[2][0] - hist[2][1]) * dd.shape[1])

# resolution of "image" plane in degrees
res_l_deg = np.rad2deg(1.22 / u_extent)
res_m_deg = np.rad2deg(1.22 / v_extent)

# in arcsec
res_l_arcsec = res_l_deg * 3600
res_m_arcsec = res_m_deg * 3600

# dirty beam in dB = dbdB
dbdB = 10*np.log10(f.real*f.real + f.imag*f.imag)
dbdB -= np.max(dbdB)

# Now let's plot a bit
plt.figure()
plt.clf()
plt.title("UV Coverage")
plt.scatter(uv[0]*lmbd, uv[1]*lmbd, s=1)
plt.xlabel("U [m]")
plt.ylabel("V [m]")

plt.figure()
plt.clf()
plt.title("UV Coverage")
plt.scatter(uv[0]/1e3, uv[1]/1e3, s=1)
plt.xlabel("U [k$\lambda$]")
plt.ylabel("V [k$\lambda$]")

plt.figure()
plt.clf()
plt.title("Synthesized (dirty) beam")
s = len(dbdB)/2
plt.imshow(dbdB, interpolation='nearest', aspect='auto',
          extent=[-res_l_deg*s, res_l_deg*s, -res_m_deg*s, res_m_deg*s])
plt.xlabel("l [deg]")
plt.ylabel("m [deg]")

plt.figure()
plt.clf()
plt.title("Synthesized (dirty) beam")
plt.imshow(dbdB, interpolation='nearest', aspect='auto',
          extent=[-res_l_arcsec*s, res_l_arcsec*s, -res_m_arcsec*s, res_m_arcsec*s])
plt.xlabel("l [arcsec]")
plt.ylabel("m [arcsec]")


# This is primary beam stuff

fwhm = np.rad2deg(1.22 * lmbd / 6.1) # 6.1m for ATA
sig = fwhm / 2.355 # sigma is better for Gaussian distribution

# Mesh the entire image
l_grid = np.linspace(-res_l_deg*s, res_l_deg*s, len(dbdB))
m_grid = np.linspace(-res_m_deg*s, res_m_deg*s, len(dbdB))
l_mesh, m_mesh = np.meshgrid(l_grid, m_grid)

# Calculate attenuation due to primary beam
att_pb = normal_dist2D(l_mesh, m_mesh, 0, sig)

# Convolve the dirty beam with the primary beam
dirty_beam_attenuated = 10*np.log10(att_pb) + dbdB

# Some more plots

# Now plot primary beam in l,m
plt.figure()
plt.clf()
plt.title("Primary beam (linear scale)")
plt.imshow(att_pb, interpolation='nearest', aspect='auto',
          extent=[-res_l_deg*s, res_l_deg*s, -res_m_deg*s, res_m_deg*s])
plt.xlabel("l [deg]")
plt.ylabel("m [deg]")

# Now plot after applying PB attenuation
# Note I am putting vmin at -40 dB to make the image slightly better
plt.figure()
plt.clf()
plt.title("Synthesized (dirty) beam w/ primary beam attenuation")
plt.imshow(dirty_beam_attenuated, interpolation='nearest', aspect='auto', vmin=-40,
          extent=[-res_l_deg*s, res_l_deg*s, -res_m_deg*s, res_m_deg*s])
plt.xlabel("l [deg]")
plt.ylabel("m [deg]")


plt.show()
