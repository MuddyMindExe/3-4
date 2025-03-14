import threading
from fileinter import DataHandling, File


class UserInteraction:
    def __init__(self):
        self.prime = 'prime.txt'
        self.factorial = 'factorial.txt'
        self.status = threading.Event()

    def generate(self):
        DataHandling
