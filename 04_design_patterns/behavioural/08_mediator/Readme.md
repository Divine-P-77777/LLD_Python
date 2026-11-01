Mediator Pattern
Imagine you're building an airport system where multiple airplanes need to coordinate for landing and takeoff. If each airplane communicates directly with every other airplane to check if the runway is clear, the system becomes extremely complicated as more planes arrive. Each pilot would need to keep track of all other planes, creating a chaotic mess of communication lines and dependencies.

let say if n = 5 and we have to make n*2



Solution using Mediator Pattern
Scenario: In an airport system, multiple airplanes communicate through a central Air Traffic Control Tower, eliminating the need for each plane to know about or track all other planes.
How it works:
Mediator: Air Traffic Control Tower
Colleagues: Airplanes send requests and messages to the control tower,
which then coordinates and relays information to other planes as needed.


Mediator Pattern Benefits
Reduces Complexity: The mediator handles all communication in one place, eliminating messy direct connections between objects.
Loose Coupling: Objects only interact with the mediator, making the code easier to modify and extend.
Single Responsibility: The mediator manages all communication logic, so individual objects can focus on their own tasks.
Centralized Control: Communication rules can be updated in the mediator without changing any of the individual objects.



Real World Use Cases
Air Traffic Control:
Airplanes communicate through a central control tower (mediator) instead of talking directly to each other.
GUI Component Coordination:
In user interface apps, different Ul elements like dropdowns, text boxes, and buttons often need to work together. When you select something in a dropdown, it might need to update a text field or enable a button. A mediator handles these interactions so the components don't need to know about each other directly.
Workflow Systems:
In business management software, a mediator can coordinate tasks acros different teams or departments, ensuring smooth communication without each team needing to directly interact with every other team.