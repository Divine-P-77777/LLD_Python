Prototype Pattern – LLD (Python)
Category: Creational Design Pattern
1. Problem Statement
Imagine building a Chess Game where you need to save the current board position for features like Undo or Save Points.

A chessboard contains multiple pieces, each having its own name, position and color.

Manually creating a new board and copying every piece individually is repetitive and difficult to maintain.
2. Solution – Prototype Pattern
The Prototype Pattern creates new objects by cloning existing objects instead of constructing them from scratch.

A clone() method is responsible for creating a copy of the existing object.



7. Main Components
Component	Responsibility
Prototype	Defines the cloning interface
Concrete Prototype	Implements the clone() method
Client	Requests a clone instead of creating a new object

8. Benefits
1. Easy Object Copying: Clone complex objects with a single method call.
2. Less Repetitive Code: Avoid manually copying attributes.
3. Flexible Copying: Choose shallow or deep copying.
4. Faster Creation: Reuse an existing object's configuration.
5. Reduced Dependencies: Client doesn't need to know the object's construction details.
9. Real-World Examples
System	Prototype Usage
Chess Game	Clone board positions for Undo
Document Editor	Duplicate existing documents
Game Development	Clone enemies and characters
Configuration Management	Duplicate configurations
UI Builder	Clone existing UI components

10. Interview Takeaway
Remember:
- Prototype creates objects by cloning existing objects.
- clone() is the central method.
- copy.copy() performs shallow copying.
- copy.deepcopy() performs deep copying.
- Deep copy is useful when nested mutable objects must also be independent.