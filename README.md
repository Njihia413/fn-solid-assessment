# SOLID Principles - Refactoring Solutions

## Task 1: Single Responsibility Principle (SRP)

### Violation in Initial Code
The `UserManager` class violates SRP by having two distinct responsibilities:
1. Managing user data (adding, retrieving, and removing users)
2. Handling email notifications

These responsibilities have different reasons to change - user management might change if storage requirements change, while email notification might change if the communication method changes.

### Refactored Solution:

```python
# Refactored code for Task 1 (SRP)
import smtplib  # Example library, no actual sending needed

class UserManager:
    def __init__(self):
        self._users = {}  # In-memory user storage

    def add_user(self, user_id, email):
        print(f"Adding user {user_id} with email {email}")
        self._users[user_id] = email

    def get_user_email(self, user_id):
        return self._users.get(user_id)

    def remove_user(self, user_id):
        if user_id in self._users:
            print(f"Removing user {user_id}")
            del self._users[user_id]


class EmailNotifier:
    """
    Removed user id as a parameter in the send notification email below
    This way, the EmailNotifier doesn't need to know anything about users
    or user IDs
    This is better SRP
    """
    def send_notification_email(self, email, message):
        if email:
            print(f"Attempting to send email to {email}: '{message}'")
            # Simulate sending email (no actual sending required)
            # Commenting out actual SMTP code to avoid errors
            # server = smtplib.SMTP('smtp.example.com')
            # server.sendmail('task2@example.com', email, f"Subject: Notification\n\n{message}")
            # server.quit()
            print("Simulated email sent.")
        else:
            print(f"Could not send email: Email not found.")


if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("user001", "johndoe@gmail.com")

    email = manager.get_user_email("user001")
    print(f"Retrieved email: {email}")

    notifier = EmailNotifier()
    notifier.send_notification_email(email, "SRP on Task 1 is done!!!")

```

## Task 2: Open/Closed Principle (OCP)

### Violation in Initial Code
The `DiscountCalculator` violates OCP because adding a new customer type (e.g., "Premium") requires modifying the existing `calculate_discount` method. The class is not "closed for modification."

### Refactored Solution:

```python
# Refactored code for Task 2 (OCP)
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

```

## Task 3: Liskov Substitution Principle (LSP)

### Violation in Initial Code
The `Square` class violates LSP because it cannot be substituted for a `Rectangle` without breaking expected behavior. When a function like `print_expected_area` sets only the width of a rectangle, it expects the height to remain unchanged. However, with a `Square`, changing the width also changes the height, leading to unexpected results.

### Refactored Solution:

```python
# Refactored code for Task 3 (LSP)
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

```

## Task 4: Interface Segregation Principle (ISP)

### Violation in Initial Code
The `IWorker` interface violates ISP because it's a "fat" interface that forces implementations to provide methods they don't need. Specifically, `RobotWorker` is forced to implement `eat()` and `sleep()` methods despite robots not needing these capabilities.

### Refactored Solution:

```python
# Refactored code for Task 4 (ISP)
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

```

## Task 5: Dependency Inversion Principle (DIP)

### Violation in Initial Code
The `NotificationService` violates DIP because it directly depends on the concrete `EmailSender` class. This creates tight coupling, making it difficult to change the notification method without modifying the service class.

### Refactored Solution

```python
# Refactored code for Task 5 (DIP)
from abc import ABC, abstractmethod


# Define abstraction (interface)
class IMessageSender(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


# Low-level module now depends on abstraction
class EmailSender(IMessageSender):
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: '{message}'")


# Alternative implementation
class SMSSender(IMessageSender):
    def send(self, recipient, message):
        print(f"Sending SMS to {recipient}: '{message}'")


# High-level module depends on abstraction, not concrete implementation
class NotificationService:
    def __init__(self, message_sender: IMessageSender):
        self._sender = message_sender

    def send_notification(self, user, contact, message):
        print(f"Processing notification for {user}...")
        self._sender.send(contact, message)


if __name__ == '__main__':
    email_sender = EmailSender()
    sms_sender = SMSSender()

    # Use email notifications
    email_service = NotificationService(email_sender)
    email_service.send_notification("John", "johndoe@gmail.com", "Your order has shipped!")

    # Easy to switch to SMS without changing NotificationService
    sms_service = NotificationService(sms_sender)
    sms_service.send_notification("John", "+1234567890", "Your order has shipped!")

```
