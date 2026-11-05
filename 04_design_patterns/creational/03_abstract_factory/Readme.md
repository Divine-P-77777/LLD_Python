Abstract Factory Pattern – LLD (Python)
Category: Creational Design Pattern
1. Problem Statement
Imagine building a food ordering application supporting multiple cuisines:
- North Indian
- South Indian
- Chinese
Each cuisine provides a family of related products:
Cuisine	Starter	Main Course	Dessert
North Indian	Paneer Tikka	Butter Chicken	Gulab Jamun
South Indian	Medu Vada	Dosa	Payasam
Chinese	Spring Rolls	Fried Rice	Fortune Cookie

Challenge: How can we switch between cuisines without changing the restaurant's meal-processing logic?



6. Main Components
Component	Responsibility
Abstract Factory	Defines methods to create a family of products
Concrete Factory	Creates a specific family of products
Abstract Products	Define common product interfaces
Concrete Products	Implement individual products
Client	Uses the factory without knowing concrete classes

7. Benefits
- Decoupling: Client doesn't depend on concrete product classes.
- OCP: Add new product families without modifying client logic.
- Consistency: Ensures related products belong to the same family.
- Flexibility: Switch entire product families at runtime.
- Maintainability: Separates object creation from business logic.
8. Factory vs Abstract Factory
Factory Pattern	Abstract Factory
Creates individual products	Creates families of related products
Usually one factory	Abstract factory with multiple concrete factories
Example: Pizza or Burger	Example: Complete North Indian or Chinese meal
Focuses on object creation	Focuses on related object families

9. Real-World Examples
System	Product Families
UI Framework	Windows UI, macOS UI
Database	MySQL Connection, Commands
E-commerce	Amazon, Flipkart payment/shipping components
Gaming	Warrior, Mage character equipment
Food Ordering	North Indian, South Indian, Chinese meals

10. Interview Takeaway
Remember:
- Abstract Factory creates families of related objects.
- Abstract Products define common interfaces.
- Concrete Factories create specific product families.
- Client depends only on the Abstract Factory interface.
- Switching factories switches the entire product family.