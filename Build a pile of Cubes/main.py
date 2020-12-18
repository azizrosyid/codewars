import unittest
from unittest import result
from math import floor, sqrt

def find_nb(m):
    n = 1
    result = 0
    while result < m:
        result += n**3
        n+=1
    returnValue = n - 1 if result == m else -1
    return returnValue

# def find_nb(m):
#     # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
#     # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
#     # so take square root and round down the result.
#     n_canidate = int(floor(sqrt(2 * sqrt(m))))
#     if (n_canidate * (n_canidate + 1) / 2 )**2 == m:
#         return n_canidate
#     else:
#         return -1

class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value

    def testing(self):
        self.assertEqual(find_nb(4183059834009), 2022)
        self.assertEqual(find_nb(24723578342962), -1)
        self.assertEqual(find_nb(135440716410000), 4824)
        self.assertEqual(find_nb(40539911473216), 3568)
        self.assertEqual(find_nb(26825883955641), 3218)


if __name__ == '__main__':
    unittest.main()
