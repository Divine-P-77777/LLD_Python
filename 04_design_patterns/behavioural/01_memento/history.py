from text_memento import TextMemento


class History:

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self, memento: TextMemento):
        self.undo_stack.append(memento)
        self.redo_stack.clear()

    def undo(self):
        if len(self.undo_stack) <= 1:
            return None

        self.redo_stack.append(self.undo_stack.pop())
        return self.undo_stack[-1]

    def redo(self):
        if not self.redo_stack:
            return None

        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento