# Memento Design Pattern

## Definition
Captures an object's state so it can be restored later
without exposing its internal implementation.

## Components

1. Originator → TextEditor
   Creates and restores snapshots.

2. Memento → TextMemento
   Stores a snapshot of the editor's state.

3. Caretaker → History
   Stores and retrieves snapshots without modifying them.

## Undo / Redo
- Undo: Move the current state to redo history.
- Redo: Restore the most recently undone state.
- New edit after undo: Clear redo history.

## Benefits
- Encapsulates saved state.
- Separates editing from history management.
- Supports undo/redo.
- Improves maintainability.

## Key takeaway
Originator owns the state.
Memento captures the state.
Caretaker manages the snapshots.