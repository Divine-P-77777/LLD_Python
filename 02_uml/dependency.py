# ## Dependency

# Dependency is a weak relationship where one class
# temporarily uses or relies on another class.

# The dependent class does NOT permanently own the
# other object.

# Dependency commonly occurs through:

# - Method parameters
# - Return types
# - Local/temporary objects
# - Method calls

# Simple meaning:

# "Class A uses Class B to do some work,
# then stops depending on it."


# A ReportService needs a Printer to print a report. (ReportService depends on Printer.)

class Printer:

    def print_document(self, document: str):
        print(f"Printing: {document}")


class ReportService:

    def generate_report(self, printer: Printer):
        report = "Monthly Sales Report"

        printer.print_document(report)


printer = Printer()

service = ReportService()

service.generate_report(printer)


# ┌──────────────────────┐
# │    ReportService     │
# ├──────────────────────┤
# │ + generate_report()  │
# └──────────────────────┘
#            - - - - - - - - - - >
#                   uses
#            - - - - - - - - - - -

# ┌──────────────────────┐
# │       Printer        │
# ├──────────────────────┤
# │ + print_document()   │
# └──────────────────────┘

# Dashed arrow = Dependency  , e.g : ReportService - - - - > Printer