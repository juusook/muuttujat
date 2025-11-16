class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super(). __init__(name)

    def print_information(self):
        super().print_information(self)
        print(f"Author: {self.author}\n"
              f"Pages: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, editor, pages):
        self.name = name
        self.editor = editor
        self.pages = pages
        super().__init__(name)

    def print_information(self):
        super().print_information(self)
        print(f"Editor: {self.editor}\n"
              f"Pages: {self.pages}")

narnia = Book("Narnia", "C.S. Lewis", 330)
narnia.print_information()

aku_ankka = Magazine("Aku Ankka", "Carl Barks", 43)
aku_ankka.print_information()
