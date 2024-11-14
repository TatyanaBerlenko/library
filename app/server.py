from flask import Flask, jsonify, render_template, request

from app.books import add_new_book, get_next_id
from books import get_book_by_id, get_all_books

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book)
    return 'The book id is invalid'


@app.route('/books')
def get_books():
    return render_template('books.html', books=get_all_books())


@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if 'title' in new_book and 'author' in new_book and 'year' in new_book and 'genre' in new_book:
        new_book['id'] = get_next_id()
        add_new_book(new_book)
        return jsonify(new_book), 201
    return "Invalid book data", 400


if __name__ == '__main__':
    app.run(port=8080)

