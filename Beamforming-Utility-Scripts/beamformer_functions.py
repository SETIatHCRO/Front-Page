import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.constants as const
from astropy.coordinates import Angle

def primary_beam_plot(center_freq1, center_freq2):
    # Primary beam diameter equation
    def primary_beam_diameter(center_freq):
        # Constants
        c = const.c  # Speed of light
        d = 6.1 * u.m  # Antenna diameter
        center_freq = center_freq * u.GHz # Assume user input in GHz
        lambda_ = c / center_freq # Wavelength
        # Primary beam diameter
        pb_diam = Angle((1.22 * lambda_ / d) * u.radian)
        return pb_diam.degree

    # Calculate primary beam diameters (in degrees) for both center frequencies
    pb_diam1 = primary_beam_diameter(center_freq1)
    pb_diam2 = primary_beam_diameter(center_freq2)

    # Calculate radius (in degrees) for both primary beams
    pb_radius1 = pb_diam1 / 2
    pb_radius2 = pb_diam2 / 2

    # Create figure and axis objects
    fig, ax = plt.subplots()

    # Add circles to the plot (to scale)
    ax.add_artist(plt.Circle((0, 0), pb_radius1, fill=False,
                  linewidth=2, edgecolor='r', label=f'{center_freq1} GHz'))
    ax.add_artist(plt.Circle((0, 0), pb_radius2, fill=False,
                  linewidth=2, edgecolor='b', label=f'{center_freq2} GHz'))

    # Set limits and aspect ratio
    ax.set_xlim([-max(pb_radius1, pb_radius2), max(pb_radius1, pb_radius2)])
    ax.set_ylim([-max(pb_radius1, pb_radius2), max(pb_radius1, pb_radius2)])
    ax.set_aspect('equal')

    # Add units to the plot
    ax.set_xlabel('Distance from primary beam center (degrees)')
    ax.set_ylabel('Distance from primary beam center (degrees)')

    # Add legend to the plot
    ax.legend()

    # Show the plot
    plt.show()
