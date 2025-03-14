import threading
from fileinter import DataHandling, File


class Await:
    def __init__(self, starter: File, prime_file: str, factorial: str):
        self.status = threading.Event()
        self.starter_file = starter
        self.dh = DataHandling(self.starter_file)
        self.prime = prime_file
        self.factorial = factorial

    def await_generation(self):
        self.dh.generate_list()
        self.status.set()

    def await_prime(self):
        self.status.wait()
        self.dh.prime_list(File(self.prime))

    def await_factorial(self):
        self.status.wait()
        self.dh.factorial_list(File(self.factorial))


def main():
    aw = Await(File(File.set_path()), 'prime.txt', 'factorial.txt')
    t1 = threading.Thread(target=aw.await_generation)
    t2 = threading.Thread(target=aw.await_prime)
    t3 = threading.Thread(target=aw.await_factorial)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

main()
