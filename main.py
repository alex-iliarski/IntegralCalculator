#Runs the integrals

import data
import simpson


# populate files we wish to use
data.write_sine_to_csv(999)

sine_points = data.Data()
sine_points.read_from_csv("sine.csv")
print(simpson.evaluate_integral(sine_points.get_points()))
# expected result is 0 for integral of sin(x) from 0 to 2pi

