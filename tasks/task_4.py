# Task 4: Interface Segregation Principle (ISP)
# ISP principle states that clients should not be forced to depend on interfaces they do not use.
# Goal: Clients should not be forced to depend on interfaces they do not use.
# Scenario: A "fat" Worker interface includes methods for working, eating, and sleeping. This forces a RobotWorker class, which doesn't eat or sleep, to implement (or ignore) these methods.

"""
The IWorker interface is a 'fat' interface that includes multiple unrelated responsibilities
This forces implementing classes to provide implementations for methods they might not use
This creates awkward implementations that essentially do nothing or print error messages.
"""
# Initial Code

# from abc import ABC, abstractmethod
#
# # "Fat" interface
# class IWorker(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#     @abstractmethod
#     def sleep(self):
#         pass
#
# # Human worker uses all methods
# class HumanWorker(IWorker):
#     def work(self):
#         print("Human working...")
#
#     def eat(self):
#         print("Human eating...")
#
#     def sleep(self):
#         print("Human sleeping...")
#
# # Robot worker only needs 'work'
# class RobotWorker(IWorker):
#     def work(self):
#         print("Robot working...")
#
#     # --- Violation Alert: Forced to implement methods it doesn't need ---
#     def eat(self):
#         # Robots don't eat
#         print("Robot cannot eat.")
#         pass # Or raise an error, but still forced dependency
#
#     def sleep(self):
#         # Robots don't sleep
#         print("Robot cannot sleep.")
#         pass # Or raise an error

# --- How it might be used ---
# human = HumanWorker()
# robot = RobotWorker()
#
# workforce = [human, robot]
#
# for worker in workforce:
#     worker.work()
#     # Trying to call eat/sleep on robot is awkward
#     # worker.eat()
#     # worker.sleep()


#Refactored code
from abc import ABC, abstractmethod


# Segregated interfaces
class IWorkable(ABC):
    @abstractmethod
    def work(self):
        pass


class IEatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class ISleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass


# Human worker implements all interfaces
class HumanWorker(IWorkable, IEatable, ISleepable):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")

    def sleep(self):
        print("Human sleeping...")


# Robot worker only implements IWorkable
class RobotWorker(IWorkable):
    def work(self):
        print("Robot working...")



if __name__ == '__main__':
    human = HumanWorker()
    robot = RobotWorker()

    workforce = [human, robot]

    for worker in workforce:
        worker.work()  # This works for both

    # For humans only
    if isinstance(human, IEatable):
        human.eat()
    if isinstance(human, ISleepable):
        human.sleep()


