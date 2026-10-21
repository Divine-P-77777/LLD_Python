from text_memento import TextMemento


class TextEditor:

    def __init__(self):
        self._text = ""

    def write(self, new_text: str):
        self._text += new_text

    def get_text(self) -> str:
        return self._text

    def save(self) -> TextMemento:
        return TextMemento(self._text)

    def restore(self, memento: TextMemento):
        self._text = memento.text