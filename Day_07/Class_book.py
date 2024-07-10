class Book:

    def __init__(self, title, author, numberOfPages):
        print("__init__ method ")
        self.title = title
        self.author = author
        self.numberOfPages = numberOfPages
 
    def display_info(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Number of Pages: {self.numberOfPages}")
 
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 195)  
book2 = Book("The Lord of the Rings", "J. R. R. Tolkien", 1138)  
 
book1.display_info()
print()
book2.display_info()  