# Undo/Redo Problem Statement
# Think of a text editor like MS Word or Google Docs.
# When you type, delete, or format text, the editor saves a "snapshot" of what the document looks like after each action.
# This way, when you press Ctrl+Z (undo), the editor can bring back the previous version of your document


from history import History
from text_editor import TextEditor


editor = TextEditor()
history = History()

# Save the initial empty state
history.save_state(editor.save())

# Write Hello
editor.write("Hello")
history.save_state(editor.save())

# Write World
editor.write(" World")
history.save_state(editor.save())

print("Current:", editor.get_text())
# Hello World

# Undo
editor.restore(history.undo())
print("After undo:", editor.get_text())
# Hello

# Redo
editor.restore(history.redo())
print("After redo:", editor.get_text())
# Hello World

# Write something new
editor.write(" Goodbye")
history.save_state(editor.save())

print("New text:", editor.get_text())
# Hello World Goodbye

# Undo again
editor.restore(history.undo())
print("After undo:", editor.get_text())
# Hello World