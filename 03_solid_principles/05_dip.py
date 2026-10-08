# D - Dependency Inversion Principle (DIP)

# Definition: High-level modules (business logic) should not depend directly on low-level modules (specific implementations).
# Both should depend on abstractions (interfaces).

# Simple terms:
# High-level = Main business logic (what your app does)
# Low-level = Specific implementations (database, email, etc.)
# Abstraction = Interface/contract between them


# Bad Example — Tight Coupling

class EmailService:

    def send_email(self, message):
        print(f"Email: {message}")


class SMSService:

    def send_sms(self, message):
        print(f"SMS: {message}")


class NotificationService:

    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def notify_by_email(self, message):
        self.email_service.send_email(message)

    def notify_by_sms(self, message):
        self.sms_service.send_sms(message)


notification = NotificationService()

notification.notify_by_email("Good morning")
notification.notify_by_sms("Hey")


# NotificationService directly creates:
# EmailService()
# SMSService()

# Good Example — Depend on Abstraction

from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotification(Notification):

    def send(self, message: str):
        print(f"Email: {message}")


class SMSNotification(Notification):

    def send(self, message: str):
        print(f"SMS: {message}")


class NotificationService:

    def __init__(self, notification: Notification):
        self.notification = notification

    def notify(self, message: str):
        self.notification.send(message)


# Dependency Injection

email_notification = EmailNotification()
sms_notification = SMSNotification()

email_service = NotificationService(email_notification)
sms_service = NotificationService(sms_notification)

email_service.notify("Good morning")
sms_service.notify("Hey")


    #                 Notification
    #                 <<abstract>>
    #                      ▲
    #             ┌────────┴────────┐
    #             │                 │
    #             │                 │
    #   EmailNotification    SMSNotification
    #             │                 │
    #             └────────┬────────┘
    #                      │
    #                      ▼
    #            NotificationService
    #                      │
    #                 notify()
    #                      │
    #                      ▼
    #               notification.send()