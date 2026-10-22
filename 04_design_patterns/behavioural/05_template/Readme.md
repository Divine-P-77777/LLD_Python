Problem Statement
Imagine you're building a system that reads data from different file types like CSV, XML, and JSON. Every file reader needs to follow the same basic process: open the file, read the content, and close the file.
If you don't use the Template Method Pattern, you'll end up writing the same opening and closing logic over and over again in each file reader class.




UML relationships
- DataParser: Abstract base class that defines the algorithm's structure.
- CSVParser: Implements the CSV-specific parsing step.
- JSONParser: Implements the JSON-specific parsing step.
- Inheritance: Both concrete parsers inherit the common workflow from DataParser.
- + means public, # means protected, and * indicates an abstract operation.

Key differences
Without Template Pattern	With Template Pattern
Common logic is duplicated	Common logic is centralized
Each class controls the workflow	Base class controls the workflow
Changes require multiple updates	Common changes require one update
