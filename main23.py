books = ["1984", "The Hobbit", "Dune", "Hamlet"]
copies = [3, 0, 5, 2]
library = {book: copy for book, copy in zip(books, copies)}
available = [book for book, copy in library.items() if copy > 0]
print("available books:", available)
choice = input("which book do you want to borrow? ")
if choice not in library or library[choice] == 0:
    print("sorry, that book is not available.")
    exit()
late_fees = [1, 2, 50, 3]
extra = float(input("enter extra late fee amount: "))
updated_fees = list(map(lambda fee: fee + extra, late_fees))
idx = books.index(choice)
print(f"updated late fee for this book: ${updated_fees[idx]}")
library[choice] = library[choice] -1
print("you have borrowed the book here are remaining copies of the book", library[choice])