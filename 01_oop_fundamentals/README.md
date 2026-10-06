# OOP Fundamentals

Object-Oriented Programming (OOP) is a programming paradigm where
software is organized around objects that contain:

- State → data/attributes
- Behavior → methods/functions

OOP helps us build software that is:

- Modular
- Reusable
- Maintainable
- Extensible
- Easier to test

## Core Concepts

1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction

These concepts form the foundation of Low-Level Design (LLD).



# Four Pillars of OOP

## 1. Encapsulation

Protect and control object state.

Data + methods → class

Example:
BankAccount → deposit(), withdraw()

---

## 2. Inheritance

Reuse/extend behavior from another class.

Example:

Vehicle
  ↓
Car

---

## 3. Polymorphism

Same interface → different behavior.

Example:

payment.pay()

Cashfree → implementation A
Stripe   → implementation B

---

## 4. Abstraction

Expose essential behavior and hide implementation details.

Example:

Payment
  ↓
pay()

Caller doesn't care how payment happens.