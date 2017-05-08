# Statisticians would like to have a set of functions to compute the median and
# mode of a list of numbers. The median is the number that would appear at the
# midpoint of a list if it were sorted. The mode is the number that appears most
# frequently in the list. Define these functions in a module named stats.py. Also
# include a function named mean, which computes the average of a set of numbers.
# Each function expects a list of numbers as an argument and returns a single
# number.


class Stats(object):
    def __init__(self, a_list):
        self.data_set = sorted(a_list)

    def mode(self):
        most = 0
        mode = 0
        for number in self.data_set:
            occ = self.data_set.count(number)
            if occ > most:
                mode = number
        return mode

    def mean(self):
        total = 0
        for number in self.data_set:
            total += number
        return total / len(self.data_set)

    def median(self):
        middle = round(len(self.data_set) / 2)
        return self.data_set[middle]
