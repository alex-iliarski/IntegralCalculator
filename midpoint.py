#Tests the Composite Midpoint Rule


import time
import math


# evaluates the integral according to the formula for the Composite Midpoint Rule
def evaluate_integral(data_pts):
    start_time = time.time()

    start = data_pts[0][0]  # x-coordinate of left bound of the interval
    stop = data_pts[-1][0]  # x-coordinate of right bound of the interval
    num_points = len(data_pts) # number of data points
    step = (stop - start) / (num_points + 2) # step size used in the Simpson method

    total = 0  # result of integration, is modified incrementally

    for j in range(0, int(num_points / 2)):
        total += data_pts[2*j][1]

    total *= (step * 2)

    end_time = time.time()
    print("Time elapsed for Composite Midpoint Rule: ")
    print(end_time - start_time)

    return total
