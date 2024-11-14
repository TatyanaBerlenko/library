from flask import Flask, jsonify
from books import get_book_by_id, get_all_books

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello! Welcome to my library'


@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book)
    return 'The book id is invalid'


@app.route('/books')
def get_books():
    return jsonify(get_all_books())


if __name__ == '__main__':
    app.run(port=8080)

