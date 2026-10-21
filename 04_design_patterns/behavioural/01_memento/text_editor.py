from text_memento import TextMemento


class TextEditor:
    def __init__(self):
         self. text = ""


    def write(self, new_text):
        self. text += new_text
    
    def get_text(self) -> str:
        return self._text
    
    def save(self) -> TextMemento:
        return TextMemento (self._text)