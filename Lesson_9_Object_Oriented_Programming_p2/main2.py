def__init__(self, list_of_books, name):
self.booksList = list_of_books
self.name = name 
self.lendDict = {}

def displayBooks(self):
    print(f"We have the following books in our library: {self.name}")
    for book in self.booksList:
        print(book)
    
def lendBook(self,user,book):
    