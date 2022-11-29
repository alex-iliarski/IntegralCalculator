#data class - represents a the data points of a mathematical function

import math


# creates csv file and writes data to it for sin(x)
def write_sine_to_csv(num_points): #TODO: generalize to any interval
    with open("sine.csv", "w") as data_file:
        for i in range(num_points):
            x = i * (2 * math.pi / num_points)  # num_points points in the interval [0, 2pi]
            y = math.sin(x)
            data_file.write(str(x) + "," + str(y) + "\n")


class Data:
    def __init__(self):
        self.pts = []  # list of data points. each point is a 2 element list

    def read_from_csv(self, file_in):
        with open(file_in, "r") as data_file:
            file_lines = data_file.readlines()

        for line in file_lines:
            point = line.split(',')

            # convert data to float, instead of string
            point[0] = float(point[0])
            point[1] = float(point[1][:-2]) # removes newline

            self.pts.append(point)  # add each point to self.pts

    def get_points(self):
        return self.pts
