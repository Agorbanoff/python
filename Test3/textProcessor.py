class TextProcessor:
    def __init__(self, text=""):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def to_uppercase(self):
        return self.text.upper()

    def to_lowercase(self):
        return self.text.lower()
