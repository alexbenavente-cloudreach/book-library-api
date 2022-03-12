from crypt import methods
from http import HTTPStatus
from http.client import NOT_FOUND
from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

books_db = [
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
        },
     {
        "id": 4
        },   

]

@app.route("/", methods=["GET"])
def home():
    return "Hello, this is my Book Library!"

@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(books_db)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books_db if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return "Book not found", HTTPStatus.NOT_FOUND

@app.route('/books', methods=["POST"])
def create_book():
    book_data = request.get_json()
    title = data.get("book title")
    author = data.get("book author")
    year = data.get("book year")
    book = {
        "id": len(books_db)+1,
        "Title": title, 
        "Author": author, 
        "Year": year
        }
    books_db.append(book)
    return jsonify(books_db), HTTPStatus.CREATED


''' 
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return "Book not found",HTTPStatus.NOT_FOUND
    
    book_data = request.get_json()
    book.update(
        {
        "Title": book_data.get("book title"), 
        "Author": book_data.get("book author"), 
        "Year": book_data.get("book year")
        }
    )
    return jsonify(book)
'''

if __name__ == "__main__":
    app.run(host="127.0.0.1")