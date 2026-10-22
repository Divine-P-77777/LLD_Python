
class CSVParser:
    def parse(self):
        self.openFile()

        # Specific logic for parsing CSV
        print("Parsing CSV File")

        self.closeFile()

    def openFile(self):
        print("Opening a file")

    def closeFile(self):
        print("Closing a file")


class JSONParser:
    def parse(self):
        self.openFile()

        # Specific logic for parsing JSON
        print("Parsing JSON File")

        self.closeFile()

    def openFile(self):
        print("Opening a file")

    def closeFile(self):
        print("Closing a file")


csv_parser = CSVParser()
csv_parser.parse()

print()

json_parser = JSONParser()
json_parser.parse()


# Problems in the code
# - Repeated code: openFile() and closeFile() are duplicated in every parser.
# - Hard to maintain: Changes to opening or closing logic must be made in every class.
# - DRY violation: Common logic is repeated unnecessarily.
# - No common workflow: Each parser independently controls the sequence of operations.