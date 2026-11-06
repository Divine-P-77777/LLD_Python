from abc import ABC, abstractmethod


# ==================================
# 1. TARGET INTERFACE
# ==================================

class NotificationService(ABC):

    @abstractmethod
    def send(self, to: str, title: str, body: str):
        pass


# ==================================
# 2. EXISTING IMPLEMENTATION
# ==================================

class EmailNotificationService(NotificationService):

    def send(self, to: str, title: str, body: str):

        print("\nSending email through EmailNotificationService")
        print(f"To: {to}")
        print(f"Title: {title}")
        print(f"Body: {body}")


# ==================================
# 3. THIRD-PARTY SERVICE
# ==================================

class SendGridEmailService:

    def send_email(self, recipient: str, subject: str, content: str):

        print("\nSending email through SendGrid")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Content: {content}")


# ==================================
# 4. ADAPTER
# ==================================

class SendGridAdapter(NotificationService):

    def __init__(self, send_grid_service: SendGridEmailService):
        self._send_grid_service = send_grid_service

    def send(self, to: str, title: str, body: str):

        # Convert the expected interface
        # into the third-party interface

        self._send_grid_service.send_email(
            recipient=to,
            subject=title,
            content=body
        )


# ==================================
# 5. CLIENT SERVICE
# ==================================

class OrderService:

    def __init__(self, email_service: NotificationService):
        self._email_service = email_service

    def create_order(self):

        self._email_service.send(
            "customer@gmail.com",
            "New Order",
            "Order has been placed"
        )


# ==================================
# 6. CLIENT
# ==================================

# Option 1: Existing Email Service

email_service = EmailNotificationService()

order_service = OrderService(email_service)
order_service.create_order()


# Option 2: Third-party SendGrid Service

send_grid_service = SendGridEmailService()

send_grid_adapter = SendGridAdapter(send_grid_service)

order_service = OrderService(send_grid_adapter)
order_service.create_order()