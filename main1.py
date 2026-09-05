class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print("you have borrowed", self.title)
    def return_book(self):
        self.is_borrowedborrowed = False
        print("you have borrowed the book", self.title)
book1 = book("red riding hood", "james")
book2 = book("the hobbit", "jack")
book3 = book("harry potter", "j.k Rowling")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()
