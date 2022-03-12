from crypt import methods
from http import HTTPStatus
from http.client import NOT_FOUND
from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

books = [
    {
        "id": 1,
        "Title": "Harry Potter and the Sorcerer's Stone", 
        "Author": "J.K. Rowling", 
        "Year": "1997"
    },
    {
        "id": 2,
        "Title": "A Christmas Carol", 
        "Author": "Charles Dickens", 
        "Year": "1843"
    },
    {
        "id": 3,
        "Title": "The Wonderful Wizard of Oz", 
        "Author": "L. Frank Baum", 
        "Year": "1900"
    }
]

@app.route("/", methods=["GET"])
def home():
    return "Hello, this is my Book Library!"

# route to list all books using the GET method
@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(books)

# route to list a book using the GET method
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return "Book not found", HTTPStatus.NOT_FOUND

# route to create a book using the POST method
@app.route('/books', methods=["POST"])
def create_book():
    book_data = request.get_json()
    title = book_data.get("Title")
    author = book_data.get("Author")
    year = book_data.get("Year")
    book = {
        "id": len(books)+1,
        "Title": title, 
        "Author": author, 
        "Year": year
        }
    books.append(book)
    return jsonify(books), HTTPStatus.CREATED

# route to update book using the PUT method
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return "Book not found",HTTPStatus.NOT_FOUND
    
    book_data = request.get_json()
    book.update(
        {
        "Title": book_data.get("Title"), 
        "Author": book_data.get("Author"), 
        "Year": book_data.get("Year")
        }
    )
    return jsonify(book)

# route to delete book using the DELETE method
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return "Book not found",HTTPStatus.NOT_FOUND
    books.remove(book)
    return jsonify(books)

if __name__ == "__main__":
    app.run(host="127.0.0.1")