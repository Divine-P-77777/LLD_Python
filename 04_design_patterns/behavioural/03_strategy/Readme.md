# Strategy Pattern in Python

## Definition

The **Strategy Pattern** is a behavioral design pattern that defines a family of algorithms, encapsulates each one in a separate class, and makes them interchangeable.

## Problem Without Strategy Pattern

- Too many `if-elif-else` statements.
- `DiscountService` decides the discount and calculates it.
- Adding new discounts requires modifying existing code.
- Difficult to test and maintain as the application grows.

## Solution

Create a `DiscountStrategy` abstract class and implement each discount in a separate class.

### Design

- `DiscountStrategy`: common interface.
- `DiwaliDiscount`, `HoliDiscount`, `RepublicDayDiscount`, `MonsoonDiscount`: concrete strategies.
- `DiscountService`: context that delegates calculations to the selected strategy.
- Client: chooses which strategy to use.

## SOLID Principles

**SRP — Single Responsibility Principle:** Each discount class handles its own calculation.

**OCP — Open/Closed Principle:** Add new discount strategies without modifying `DiscountService`.

## Advantages

1. Removes festival-specific if-else chains.
2. Makes discount algorithms interchangeable.
3. Simplifies independent unit testing.
4. Improves readability and maintainability.
5. Makes adding new discount types easier.

## Run the Project

Run the example:

```bash
python good_example.py
```

Run the unit tests:

```bash
python -m unittest -v test_discounts.py
```

## Key Takeaway

**Without Strategy Pattern:** Add a new discount → modify existing conditional logic.

**With Strategy Pattern:** Add a new discount → create a new strategy class.

The client still needs a way to select the appropriate strategy, but the discount calculation logic remains independent of the service.
