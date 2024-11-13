books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Fiction"
    },
    {
        "id": 2,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "genre": "Romance"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Tragedy"
    },
    {
        "id": 4,
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "year": 1851,
        "genre": "Adventure"
    }
]

def get_book_by_id(_id):
    for book in books:
        if book["id"] == _id:
            return book


def get_all_books():
    return books