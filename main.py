#Runs the integrals


import data
import simpson
import trapezoid
import midpoint


# populate files we wish to use
data.write_sine_to_csv(1000)

sine_points = data.Data()
sine_points.read_from_csv("sine.csv")

# TODO: IMPLEMENT WAY TO TEST THE TIME IT TAKES TO RUN
# expected result is 0 for integral of sin(x) from 0 to 2pi

simpson_approx = simpson.evaluate_integral(sine_points.get_points())
print("Composite Simpson's Rule Approximation: (Expected value is 0)")
print(str(simpson_approx) + "\n\n")

trapezoid_approx = trapezoid.evaluate_integral(sine_points.get_points())
print("Composite Trapezoidal Rule Approximation: (Expected value is 0)")
print(str(trapezoid_approx) + "\n\n")

midpoint_approx = midpoint.evaluate_integral(sine_points.get_points())
print("Composite Midpoint Rule Approximation: (Expected value is 0)")
print(str(midpoint_approx) + "\n\n")




