# S - Single Responsibility Principle (SRP)
# Definition: A class should have only one reason to change, meaning it should do only one job or have only one responsibility.
# Simple terms: "Don't make one class do everything. Each class should focus on one task only."
# Example: A User class should only handle user-related data, while database operations should be handled by a separate UserRepository class.


# Bad Example — Multiple Responsibilities
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print("Saving user to database")

    def send_email(self):
        print("Sending email")

    def generate_report(self):
        print("Generating user report")

# Good Example — Separate Responsibilities        
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:

    def save(self, user: User):
        print("Saving user to database")


class EmailService:

    def send_welcome_email(self, user: User):
        print(f"Sending email to {user.email}")


class UserReport:

    def generate(self, user: User):
        print(f"Generating report for {user.name}")

        ## SRP

# Bad:

# User
#  ├── Data
#  ├── Database
#  ├── Email
#  └── Reports

# Multiple responsibilities ❌


# Good:

# User              → User data
# UserRepository    → Database
# EmailService      → Email
# UserReport        → Reports

# Single responsibility ✅


# Key Question:

# "Does this class have more than one
# reason to change?"

# If YES → consider separating responsibilities.