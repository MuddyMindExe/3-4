from calculations import Calculations
from time import sleep


class File:
    def __init__(self, path):
        self.path = path

    def write(self, info):
        with open(self.path, 'w') as file:
            file.write(info)

    def read(self):
        with open(self.path, 'r') as file:
            return file.readlines()


class DataHandling:
    def __init__(self):
        self.path = DataHandling.set_path()
        self.file = File(self.path)

    @staticmethod
    def set_path():
        while True:
            path = input("Input path to file and file name:\n")
            try:
                open(path, 'w').close()
                return path
            except (OSError, FileNotFoundError) as e:
                print(f"Error: {e}. Try again.")

    def generate_list(self):
        almost_random_digits = [4, 2, 5, 6, 1, 3, 9, 9]
        self.file.write(', '.join([str(el) for el in almost_random_digits]))

    def prime_list(self, file):
        primes = []
        nums = self.file.read()[0].split(', ')
        for num in nums:
            if Calculations(int(num)).is_prime():
                primes.append(int(num))
                sleep(0.001)
        primes = ', '.join([str(el) for el in primes])
        file.write(primes)

    def factorial_list(self, file):
        factorials = []
        nums = self.file.read()[0].split(', ')
        for num in nums:
            factorials.append(Calculations(int(num)).get_factorial())
            sleep(0.001)
        factorials = ', '.join([str(el) for el in factorials])
        file.write(factorials)
