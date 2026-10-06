UML Diagrams
UML (Unified Modeling Language) is a standard way to visually design and represent software systems using diagrams.
The main purpose is to have a common visual language that shows how classes, objects, relationships, and interactions work in a system.
This makes it easier for developers and teams to understand, discuss, and plan the system before writing actual code.


UML Diagrams Importance

Visualization: UML diagrams let you see the system visually, like a blueprint. This makes it much easier to understand how different parts of the system are structured, how they connect, and how they work together.

Documentation: UML diagrams act as detailed documentation of your software design. This is very helpful when you need to maintain the code later or when the system needs to grow bigger.

Communication: UML diagrams create a common language that designers, developers, and teams can all understand. Everyone can look at the same diagram and discuss the design clearly without confusion.

Standardization: Since UML is a universally accepted standard, everyone in the software industry reads and understands these diagrams the same way. No matter where you work, UML will be the same.

# LLD Quick Revision

## Association

General relationship / interaction.

User ─── Order

"User interacts with Order"


## Inheritance

IS-A relationship.

Dog ───▷ Animal

"Dog is an Animal"


## Composition

Strong HAS-A relationship.

Car ◆── Engine

"Car strongly owns Engine"


## Aggregation

Weak HAS-A relationship.

Classroom ◇── Student

"Classroom has Students,
but Students can exist independently"


## Interface / Implementation

Contract implemented by a class.

Loginable
    △
    │
   User

"User implements Loginable"