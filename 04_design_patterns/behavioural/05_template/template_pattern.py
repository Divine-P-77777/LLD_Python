
from abc import ABC, abstractmethod


class DataParser(ABC):
    # Template method: defines the algorithm's sequence
    def parse(self):
        self._open()
        self._dataParser()
        self._close()

    def _open(self):
        print("Opening a file")

    def _close(self):
        print("Closing a file")

    @abstractmethod
    def _dataParser(self):
        pass


class CSVParser(DataParser):
    def _dataParser(self):
        print("Parsing CSV File")


class JSONParser(DataParser):
    def _dataParser(self):
        print("Parsing JSON File")


csv_parser = CSVParser()
csv_parser.parse()

print()

json_parser = JSONParser()
json_parser.parse()

# How it works
# 1. DataParser defines the common algorithm in parse().
# 2. _open() and _close() contain reusable common logic.
# 3. _dataParser() is an abstract method implemented by each subclass.
# 4. CSVParser and JSONParser provide their own parsing logic.
# 5. Both parsers follow the same sequence: Open → Parse → Close.