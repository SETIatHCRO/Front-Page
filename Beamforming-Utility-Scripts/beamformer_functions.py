import numpy as np
import matplotlib.pyplot as plt

def primary_beam_plot(center_freq1, center_freq2):
    # Primary beam diameter equation
    def primary_beam_diameter(center_freq):
        # Constants
        c = 299792458  # Speed of light [m/s]
        d = 25  # Antenna diameter [m]
        lambda_ = c / (center_freq * 1e9)  # Wavelength [m]
        # Primary beam diameter [arcsec]
        return 1.22 * lambda_ * (180 / np.pi) * (1 / d) * 3600

    # Generate theta values (in arcsec) for the primary beam circle
    theta = np.linspace(0, 360, 1000)

    # Calculate primary beam diameters (in arcsec) for both center frequencies
    pb_diam1 = primary_beam_diameter(center_freq1)
    pb_diam2 = primary_beam_diameter(center_freq2)

    # Calculate radius (in arcsec) for both primary beams
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

    # Add legend to the plot
    ax.legend()

    # Show the plot
    plt.show()


primary_beam_plot(1.4, 3.0)
