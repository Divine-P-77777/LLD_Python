State Pattern


Imagine you're creating a DirectionService class for a maps application like Google Maps. This service needs to calculate how long (ETA) it will take to reach your destination and what route (directions) to follow between two locations. The travel time and route change depending on your chosen mode of transport:
Walking
Cycling
Car
Direction Service



6. Main Components
Component	Responsibility
Context	Maintains the currently active state
State	Defines a common interface
Concrete State	Implements state-specific behavior
Client	Creates or changes the active state

7. Benefits
- OCP: Add new states without modifying the Context.
- Encapsulation: Each state manages its own behavior.
- Clean Code: Eliminates complex conditional statements.
- Flexibility: Change behavior dynamically at runtime.
- Maintainability: State-specific logic stays separated.
8. Real-World Examples
System	States
Music Player	Playing, Paused, Stopped
Order Tracking	Placed, Shipped, Delivered
ATM	Idle, Card Inserted, PIN Verified
Traffic Light	Red, Yellow, Green

9. Interview Takeaway
Remember:
- Context maintains the current state.
- State defines the common interface.
- Concrete States implement different behaviors.
- Context delegates operations to the active state.