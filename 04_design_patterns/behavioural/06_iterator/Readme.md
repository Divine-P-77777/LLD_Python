Problem Statement
Imagine you're working with different data structures like arrays, lists, or trees, and you want to go through each element one by one. If you don't use the Iterator pattern, anyone using your collection must know its internal organization. Each type of collection would need its own unique way to loop through items.

7. Benefits
- Encapsulation: Hides internal collection structure.
- Separation: Separates traversal logic from collection logic.
- Consistency: Same interface for different collections.
- Flexibility: Supports forward, backward and filtered iteration.


Remember: The Collection knows how to create an Iterator; the Iterator knows how to traverse the Collection; the Client only interacts with the Iterator interface.

Python note: Python also provides built-in iteration using iter() and next(), along with the __iter__() and __next__() methods.