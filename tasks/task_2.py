# Task 2: Open/Closed Principle (OCP)
# OCP principle states that objects or entities should be open for extension but closed for modification
# Goal: Design code that is open for extension but closed for modification.
# Scenario: The DiscountCalculator calculates discounts based on customer type. Adding a new customer type (e.g., "Premium") requires modifying the calculate_discount method.

"""
The calculate_discount method contains a series of if-else statements that check the
customer_type parameter.
Adding a new customer type requires modifying the existing calculate discount method.
This way the class is not closed for modification.
"""

# Initial Code
# class DiscountCalculator:
#     def calculate_discount(self, customer_type, amount):
#         discount = 0
#         if customer_type == "Regular":
#             discount = amount * 0.05  # 5% discount
#             print(f"Applying 5% regular discount: {discount}")
#         elif customer_type == "VIP":
#             discount = amount * 0.15  # 15% discount
#             print(f"Applying 15% VIP discount: {discount}")
#         # --- Violation Alert: Adding a 'Premium' type requires modifying this method ---
#         # elif customer_type == "Premium":
#         #     discount = amount * 0.10
#         #     print(f"Applying 10% premium discount: {discount}")
#         return discount


# --- How it might be used ---
# calculator = DiscountCalculator()
# regular_discount = calculator.calculate_discount("Regular", 100)
# vip_discount = calculator.calculate_discount("VIP", 100)



#Refactored code

from abc import ABC, abstractmethod

# Abstract the base class for discount strategies
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount):
        pass


class RegularDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        discount = amount * 0.05  # 5% discount
        print(f"Applying 5% regular discount: {discount}")
        return discount


class VIPDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        discount = amount * 0.15  # 15% discount
        print(f"Applying 15% VIP discount: {discount}")
        return discount


# New discount type can be added without modifying existing code
class PremiumDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        discount = amount * 0.10  # 10% discount
        print(f"Applying 10% premium discount: {discount}")
        return discount


class DiscountCalculator:
    def __init__(self):
        self._strategies = {
            "Regular": RegularDiscount(),
            "VIP": VIPDiscount(),
            "Premium": PremiumDiscount()  # New type added without changing calculate_discount
        }

    def calculate_discount(self, customer_type, amount):
        strategy = self._strategies.get(customer_type)
        if strategy:
            return strategy.calculate_discount(amount)
        return 0  # No discount for unknown customer types


if __name__ == "__main__":
    calculator = DiscountCalculator()
    regular_discount = calculator.calculate_discount("Regular", 100)
    vip_discount = calculator.calculate_discount("VIP", 100)
    premium_discount = calculator.calculate_discount("Premium", 100)
