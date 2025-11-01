class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"name: {self.name}, author: {self.author}, page count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"name: {self.name}, chief editor: {self.chief_editor}")

pub = Publication("Test Publication")
print(f"Publication: {pub.name}")

book = Book("Test Book", "Test Author", 150)
print(f"Book: {book.name} by {book.author}, {book.page_count} pages")

mag = Magazine("Test Magazine", "Test Editor")
print(f"Magazine: {mag.name}, chief editor: {mag.chief_editor}")

donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
print(f"Name: {donald_duck.name}, Chief Editor: {donald_duck.chief_editor}")

compartment = Book("Compartment No. 6", "Rosa Liksom", 192)
print(f"Name: {compartment.name}, Author: {compartment.author}, Pages: {compartment.page_count}")