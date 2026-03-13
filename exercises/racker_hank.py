# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy


def calc_median(my_array):
    mean_array = numpy.array(my_array)
    print(numpy.mean(mean_array, axis = 0))
    print(numpy.mean(mean_array, axis = 1))
    print(numpy.mean(mean_array, axis = None))

if __name__ == '__main__':
    n = ([[2, 1, 3], [2, 2, 4]])
    calc_median(n)
