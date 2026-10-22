Problem Statement
Imagine you're building a restaurant management system. Customers can order different food items like Burger, Pizza, and Pasta.
Without Command Pattern, the Waiter class would directly call the Chef's cooking methods based on what the customer orders.
This creates tight coupling between the Waiter and the Chef.
The Waiter would need to know:
What items the Chef can cook
Exactly which method to call for each item
How to handle each specific food type



# 3. Key components to remember
# Component	Responsibility
# Command	Defines the execute() interface
# Concrete Command	Implements a specific request
# Receiver	Performs the actual work (Chef)
# Invoker	Executes the command (Waiter)
# Client	Creates and connects objects (main.py)


Why use the Command Pattern?
- Loose coupling: Waiter does not need to know Chef's methods.
- Extensibility: Add new orders without modifying Waiter.
- Open/Closed Principle: Open for extension, closed for modification.
- Reusability: Commands can be passed around and executed later.
- Advanced features: Supports undo, redo, queuing, logging, and scheduling.