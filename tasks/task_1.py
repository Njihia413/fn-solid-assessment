# Task 1: Single Responsibility Principle (SRP)
# SRP principle states that a class should have one and only one reason to change, meaning that a class should only have one job.
# Goal: Refactor code so that each class has only one reason to change.
# Scenario: The UserManager class below handles both user data storage and sending notification emails.

""""
This class handles two jobs one, updating user details using CRUD functionalities
The second one is that it handles email notifications
"""

# Initial Code

# class UserManager:
#     def __init__(self):
#         self._users = {} # In-memory user storage
#
#     def add_user(self, user_id, email):
#         print(f"Adding user {user_id} with email {email}")
#         self._users[user_id] = email
#
#     def get_user_email(self, user_id):
#         return self._users.get(user_id)
#
#     def remove_user(self, user_id):
#         if user_id in self._users:
#             print(f"Removing user {user_id}")
#             del self._users[user_id]
#
#     # --- This part violates SRP ---
#     def send_notification_email(self, user_id, message):
#         email = self.get_user_email(user_id)
#         if email:
#             print(f"Attempting to send email to {email}: '{message}'")
#             # Simulate sending email (no actual sending required)
#             # server = smtplib.SMTP('smtp.example.com')
#             # server.sendmail('from@example.com', email, f"Subject: Notification\n\n{message}")
#             # server.quit()
#             print("Simulated email sent.")
#         else:
#             print(f"Could not send email: User {user_id} not found.")



# Refactored code
"""
The send notification email function should be in another class.
This way SRP is maintained where only one class has only one job.
Class UserManager only handles user management functions.
Cass EmailNotifier handles email notifications functions.
"""
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
