# import [name_of_brandon's_script] as python_file_with_functions -> placeholder for now!
import astropy.units as u
import math

# here are the different inputs we'll try
f1 = 1.0 #GHz
f2 = 5.354 #Ghz
f3 = 11.0 #GHz

#check that the primary-beam diameter-getting function works
assert python_file_with_functions.function_to_calculate_primary_beam_diameter(f1) == math.isclose(3.5, abs_tol=0.0001), "result was not a float within 0.0001 of the correct answer in degrees"
assert python_file_with_functions.function_to_calculate_primary_beam_diameter(f2) == math.isclose(0.6537, abs_tol=0.0001), "result was not a float within 0.0001 of the correct answer in degrees"
assert python_file_with_functions.function_to_calculate_primary_beam_diameter(f3) == math.isclose(0.3333, abs_tol=0.0001),  "result was not a float within 0.0001 of the correct answer in degrees"


#Make a plot. On visual inspection...
# 1) Is the plotted diameter of f1 11X smaller than the plotted diameter of f2?
# 2) Are the units in degrees?
# 3) Is there a legend with the correct beams labelled?
python_file_with_functions.beam_comparison_plotter(f1, f3)

# 4) Can it handle it if the frequencies are put in "backwards" (highest first)? (should look exactly the same as the other plot)
python_file_with_functions.beam_comparison_plotter(f3, f1)
