from flask import Flask, abort, request
from db import authors, books

app = Flask(__name__)

#get authors by ID
def get_next_author_id():
    if authors:
        Author_list = [author["id"] for author in authors.values()]
        return max(Author_list) + 1
    else:
        return 1
# Get the next available ID for books
def get_next_book_id():
    if books:
        Book_list = [book["id"] for book in books.values()]
        return max(Book_list)+ 1
    else:
        return 1
    

#get author
@app.get("/author")
def get_authors():
    return {"Authors name": list(authors.values())}

#create endpoint for - get authors by ID
@app.get("/author/<int:author_id>")
def get_author(author_id):
    try:
        return authors[author_id]
    except KeyError:
        return{"message":"author not found."}, 404


#post author
@app.post("/author")
def create_author():
    author_data = request.get_json()
    if "name" not in author_data:
        print('author name not found in request data')
        abort(
            400,
            "Bad request. Ensure 'name' is included in the JSON payload.",
        )
    for author in authors.values():
        if author_data["name"] == author["name"]:
            print('author already exists')
            abort(400, "author already exists.")
    author_id = get_next_author_id()
    author = {**author_data, "id": author_id}
    authors[author_id] = author
    return author


# Delete the author by author id
@app.delete("/author/<int:author_id>")
def deleteAuthor(author_id):
    if author_id in authors:
        del authors[author_id]
        msg = deleteAuthorBooks(author_id)
        return f"{author_id} is deleted successfully \n" + msg, 200
    else:
        return {"message":"Author not found"}, 404
 
 
def deleteAuthorBooks(author_id):
    count = 0
    tempBooks = books.copy()
    for book in tempBooks.values():
        if book["author_id"] == author_id:
            del books[book["id"]]
            count+=1
    return f"{count} books of the author : {author_id} is also deleted sucessfully"


#get book
@app.get("/book")
def get_all_books():
    return {"books": list(books.values())}

@app.get("/book/<int:book_id>")
def get_book(book_id):
    try:
        return books[book_id]
    except KeyError:
        abort(404,"author not found.")

@app.post("/book")
def create_book():
    book_data = request.get_json()
    if (
        "price" not in book_data
        or "author_id" not in book_data
        or "name" not in book_data
    ):
        abort(
            400,
            "Bad request. Ensure 'price', 'author_id', and 'name' are included in the JSON payload.",
        )
    for book in books.values():
        if (
            book_data["name"] == book["name"]
            and book_data["author_id"] == book["author_id"]
        ):
            abort(400, "book already exists.")
    book_id = get_next_book_id()
    book = {**book_data, "id": book_id}
    books[book_id] = book
    return book


#delete endpoint fbook

@app.delete("/book/<int:book_id>")
def delete_book(book_id):
    try:
        del books[book_id]
        return {"message": "book deleted successfully."}
    except KeyError:
        abort(404,"book not found.")
 
 # update the book data
@app.put("/book/<int:book_id>")
def updateBook(book_id):
    book_data = request.get_json()
    if ("price" not in book_data or "author_id" not in book_data or "name" not in book_data):
        abort(400, message="Bad request. Ensure 'price', 'author_id', and 'name' are included in the JSON payload.")
    for book in books.values():
        if (book["id"] == book_id):
            del books[book_id]
            books[book_id] = {**book_data}
            return book
    return "book not found"

