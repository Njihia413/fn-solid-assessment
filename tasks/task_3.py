# Task 3: Liskov Substitution Principle (LSP)
# LSP principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
# Goal: Ensure that subclasses can be substituted for their base classes without errors or unexpected behavior.
# Scenario: A classic example. We have a Rectangle class and a Square class that inherits from it. Setting the width or height of a Square should logically set both dimensions equally, but this can violate expectations if a function expects a generic Rectangle.

# Initial Code

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     def calculate_area(self):
#         return self._width * self._height
#
# class Square(Rectangle):
#     def __init__(self, size):
#         super().__init__(size, size)
#
#     @Rectangle.width.setter
#     def width(self, value):
#         self._width = value
#         self._height = value # Side effect: changes height too
#
#     @Rectangle.height.setter
#     def height(self, value):
#         self._width = value # Side effect: changes width too
#         self._height = value
#
# # --- Function that expects a Rectangle ---
# def print_expected_area(rectangle: Rectangle):
#     # Let's test setting width and calculating area
#     original_height = rectangle.height
#     rectangle.width = 20
#     expected_area = 20 * original_height
#     actual_area = rectangle.calculate_area()
#     print(f"Expected Area: {expected_area}, Actual Area: {actual_area}")
    # If LSP is violated, actual_area might not match expected_area for a Square

# --- How it might be used ---
# rect = Rectangle(10, 5)
# sq = Square(10)
#
# print("Testing Rectangle:")
# print_expected_area(rect) # Output should match
#
# print("\nTesting Square:")
# print_expected_area(sq)   # Output might NOT match if LSP is violated


# Refactored code
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def calculate_area(self):
        return self._width * self._height


class Square(Shape):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def calculate_area(self):
        return self._size * self._size


def print_area(shape: Shape):
    print(f"Area: {shape.calculate_area()}")


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    sq = Square(10)

    print("Testing Rectangle:")
    print_area(rect)

    print("\nTesting Square:")
    print_area(sq)
