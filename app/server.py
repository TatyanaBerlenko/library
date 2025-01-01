from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from logger import Logger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
logger = Logger()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/<name>')
def home(name='Guest'):
    logger.info(f'Visited home page by {name}')
    return render_template('index.html', name=name)


@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get(book_id)
    logger.info(f'Visited book: {book.title}')
    if book:
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author,
        })
    return 'The book id is invalid', 404


@app.route('/books')
def get_books():
    logger.info('Visited books page')
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    logger.info('Visited add book page')
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        logger.info(f'Added new book: {title} by {author}')
        return redirect(url_for('get_books'))

    return render_template('add_book.html')


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    logger.info(f'Visited edit book page for {book.title}')
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        db.session.commit()
        logger.info(f'Edited book: {book.title} by {book.author}')
        return redirect(url_for('get_books'))
    return render_template('edit_book.html', book=book)


@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    logger.info(f'Visited delete book page for {book.title}')
    db.session.delete(book)
    db.session.commit()
    logger.info(f'Deleted book: {book.title}')
    return redirect(url_for('get_books'))


if __name__ == '__main__':
    app.run(port=8080)

