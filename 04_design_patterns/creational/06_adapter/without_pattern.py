from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send(self, to: str, title: str, body: str):
        pass


class EmailNotificationService(NotificationService):

    def send(self, to: str, title: str, body: str):
        print("Sending email through EmailNotificationService")
        print(f"To: {to}")
        print(f"Title: {title}")
        print(f"Body: {body}")


# Third-party service
class SendGridEmailService:

    def send_email(self, recipient: str, subject: str, content: str):
        print("Sending email through SendGrid")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Content: {content}")


# Client Service
class OrderService:

    def __init__(self, email_service: NotificationService):
        self._email_service = email_service

    def create_order(self):
        self._email_service.send(
            "customer@gmail.com",
            "New Order",
            "Order has been placed"
        )


# Existing implementation works
email_service = EmailNotificationService()
order_service = OrderService(email_service)
order_service.create_order()


# This fails because SendGrid has no send() method
send_grid_service = SendGridEmailService()
order_service = OrderService(send_grid_service)
order_service.create_order()