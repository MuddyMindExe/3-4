from math import sqrt, factorial


class Calculations:
    def __init__(self, num: int):
        self.num = num

    def is_prime(self):
        if self.num < 2:
            return False
        for i in range(2, int(sqrt(self.num)) + 1):
            if self.num % i == 0:
                return False
        return True

    def get_factorial(self):
        return factorial(self.num)
