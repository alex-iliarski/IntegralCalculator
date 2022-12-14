#Tests the Composite Simpson's Rule


import time


# evaluates the integral according to the formula for the Composite Simpson's Rule
def evaluate_integral(data_pts):
    start_time = time.time()

    start = data_pts[0][0]  # x-coordinate of left bound of the interval
    stop = data_pts[-1][0]  # x-coordinate of right bound of the interval
    num_points = len(data_pts) # number of data points
    step = (stop - start) / num_points # step size used in the Simpson method

    total = 0  # result of integration, is modified incrementally

    for j in range(1, int(num_points / 2)):
        total += 2 * data_pts[2 * j][1]

    for j in range(1, int(num_points / 2) + 1):
        total += 4 * data_pts[(2 * j) - 1][1]

    total += data_pts[0][1]
    total += data_pts[-1][1]

    total *= (step / 3)

    end_time = time.time()
    print("Time elapsed for Composite Simpson's Rule: ")
    print(end_time - start_time)

    return total
