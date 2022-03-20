from crypt import methods
from http import HTTPStatus
from http.client import NOT_FOUND
from flask import Flask, request, Response, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'books'
app.config['MYSQL_DB'] = 'book_db'

mysql = MySQL(app) 

# books = [
#     {
#         "id": 1,
#         "Title": "Harry Potter and the Sorcerer's Stone", 
#         "Author": "J.K. Rowling", 
#         "Year": "1997"
#     },
#     {
#         "id": 2,
#         "Title": "A Christmas Carol", 
#         "Author": "Charles Dickens", 
#         "Year": "1843"
#     },
#     {
#         "id": 3,
#         "Title": "The Wonderful Wizard of Oz", 
#         "Author": "L. Frank Baum", 
#         "Year": "1900"
#     }
# ]

@app.route("/", methods=["GET"])
def home():
    return "Hello, this is my Book Library!"

# route to list all books using the GET method
@app.route("/books", methods=["GET"])
def list_books():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * from Books ''')
    data = cursor.fetchall()

    cursor.close()
    return json.dumps(data)

# route to list a book using the GET method
@app.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM Books WHERE book_id=%s ''', book_id)
    data = cursor.fetchone()

    cursor.close()
    return json.dumps(data)

# route to create a book using the POST method
@app.route('/books', methods=["POST"])
def create_book():
    new_book = request.get_json()

    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO Books VALUES(null, %s, %s, %s) ''', (new_book["title"],new_book["author"], new_book["year"]))
    mysql.connection.commit()
    cursor.close()

    return "Book was added successfully."

# route to update book using the PUT method
@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    book_data = request.get_json()

    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE Books SET title=%s, author=%s, year=%s WHERE book_id=%s ''', (book_data["title"],book_data["author"], book_data["year"], book_id))
    mysql.connection.commit()
    cursor.close()

    return "Book was updated successfully."

# route to delete book using the DELETE method
@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM Books WHERE book_id=%s ''', book_id)
    mysql.connection.commit()
    cursor.close()

    return "Book was deleted successfully."

if __name__ == "__main__":
    app.run(host="127.0.0.1")