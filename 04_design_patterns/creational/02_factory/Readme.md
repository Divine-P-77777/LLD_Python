1. Problem Statement
Imagine building a Restaurant Ordering System where customers can order different food items:
- Pizza
- Burger
- Pasta
If RestaurantService directly creates objects using if-elif, it becomes tightly coupled to concrete food classes.



# Factory pattern basically helps us to make the object automatically




6. Main Components
Component	Responsibility
Product	Defines common interface (Food)
Concrete Product	Implements product (Pizza, Burger)
Factory	Creates appropriate objects
Client	Requests objects through the factory

7. Benefits
- Decoupling: Client doesn't directly create concrete objects.
- Centralized Creation: Object creation logic stays in one place.
- Maintainability: Easier to manage object creation.
- Flexibility: Supports different product types.


8. Real-World Examples
System	Factory Creates
Payment System	UPI, Card, Net Banking
Notification System	Email, SMS, Push
Database System	MySQL, PostgreSQL
Document Editor	PDF, Word, Excel