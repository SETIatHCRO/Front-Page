A separate output file is produced for each antenna, placed in the current directory.  The format of the name of the output file is:

        [antenna]_Results.csv

The first line of each file are labels describing the contents of columns in the file.  The second column differ between a point source and the Moon:

    Frequency :     in GHz

    L (Moon):       Convolution factor that takes into consideration the size
                    of the ATA beam and the changing angular size of the Moon.
                    Uses the Bessel approximation to the beam shape, not the
                    Gaussian approximation, since the ratio of the
                    Moon's diameter to the beam approaches the beam's first
                    null at high frequencies.  L is *defined* as
                    T_a/T_b/eta_a, where T_b is the expected Moon's
                    brightness temperature (assumed 230K, regardless of Lunar
                    phase and frequency), eta_a is the aperture efficiency,
                    T_a is the expected antenna temperature.  Used to
                    convert expected T_b to expected T_a/eta_a
                    which, when combined with the measured powers produces
                    Tsys/eta_a = (P_Sig/P_ref-1)*L*T_b.  Calculated
                    from BeamShapes.tcl for the FWHM=Freq/207' of the
                    ATA dishes and an approximate angular diameter of the
                    Moon at the mid UTC of the observations.

                    (If the Moon were to fill the beam to its first null,
                    then L = the ratio of main beam efficiency to aperture
                    efficiency, ~1.17 for the assumed 13 dB feed
                    illumination.)

    S (Point Source): Source Flux density in Jy, from the latest articles
                    by Butler & Peerly.

    MW_On MW_Off :  Expected contribution to Tsys from the Milky Way for the
                    On and Off phases.  Differences between these values
                    should influence the results *but are not included* in
                    these results. Not corrected for atmospheric attenuation
                    Derived from tsky.tcl.  Units in K

    TatmTcmb_On, TatmTcmb_off : Contributions to Tsys from the atmospheric
                    conditions at the time and elevation of the On and Off,
                    plus the contribution from the CMB.  Differences between
                    these values should influence derived SEFD *but are not
                    included* in these results.  Atmosphere value derived from
                    forecastCmdLine.tcl.  Units in K

    AtmosAtten_On   The atmospheric attenuation, exp(-tau*Air Mass), for
                    the atmospheric conditions at the time and elevation of
                    the 'off' source observation, derived from forecastCmdLine.

    Tau, Tatm       The atmospheric zenith opacity and representative
                    atmospheric temperature for the 'off' observation,
                    derived from forecastCmdLine.  Tatm is in K.

    ElevOff         The elevation of the 'off' observation, in degrees.

    P_On_[pol]_[trial] P_Off_[pol]_[trial] :  Series of columns of the raw
                    values in the input files, scaled down by 1e6 just to
                    make the range of values easier to read.

    TSYSdivEta_[pol]_trial] : Series of columms giving the derived
                    values for T_sys/eta_a.  Units in K. For Moon,
                    assumes T_b = 230 K, regardless of Lunar phase and
                    frequency, which should be accurate to about 10 K (4%).
                    For a point source, uses SEFD/(pi*DishDiam^2)/4.

    SEFD_[pol]_[trial] :  Series of columms giving the derived values
                    for SEFD, assuming the 6.1m diameter, D, of the ATA
                    dishes.  SEFD = TSys/eta_a * 2k / pi*(D/2)^2 for the
                    Moon or SEFD = S * P_Off/(P_on-P_off) for a point source.
