# Початковий код
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class SuperWorker(Worker):
    def work(self):
        print("Super working")

    def eat(self):
        print("Super eating")

# Оптимізований код з використанням ISP
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    pass

class SuperWorker(Workable, Eatable):
    def work(self):
        print("Super working")

    def eat(self):
        print("Super eating")
