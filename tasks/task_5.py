# Task 5: Dependency Inversion Principle (DIP)
# DIP principle states that high level modules should not depend on low level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.
# Goal: High-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.
# Scenario: A high-level NotificationService directly creates and uses a low-level EmailSender instance. This tightly couples the service to a specific implementation (email).

# Initial Code

# Low-level module (concrete implementation)
# class EmailSender:
#     def send(self, recipient, message):
#         print(f"Sending email to {recipient}: '{message}'")
#         # Actual email sending logic would go here

# --- Violation Alert: High-level module depends directly on low-level module ---
# High-level module
# class NotificationService:
#     def __init__(self):
#         # Direct dependency on the concrete EmailSender
#         self._sender = EmailSender()
#
#     def send_notification(self, user, message):
#         print(f"Processing notification for {user}...")
#         # Tightly coupled to EmailSender
#         self._sender.send(f"{user}@example.com", message)

# --- How it might be used ---
# service = NotificationService()
# service.send_notification("Alice", "Your order has shipped!")
# What if we want to use SMS instead? Requires changing NotificationService.


#Refactored code
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
        # Actual email sending logic would go here


# Alternative implementation
class SMSSender(IMessageSender):
    def send(self, recipient, message):
        print(f"Sending SMS to {recipient}: '{message}'")
        # Actual SMS sending logic would go here


# High-level module depends on abstraction, not concrete implementation
class NotificationService:
    def __init__(self, message_sender: IMessageSender):
        # Dependency injected through constructor
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
