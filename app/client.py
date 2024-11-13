import requests

BASE_URL = 'http://127.0.0.1:5000'


def get_home():
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        return response.text
    return f"Error: {response.status_code}"


def get_book_by_id(book_id):
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "The book id is invalid"
    return f"Error: {response.status_code}"


def get_all_books():
    response = requests.get(f"{BASE_URL}/books")
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code}"


if __name__ == '__main__':
    print("Home Page:")
    print(get_home())

    print("\nAll Books:")
    books = get_all_books()
    if isinstance(books, list):
        for book in books:
            print(book)
    else:
        print(books)

    print("\nBook by ID (ID = 1):")
    print(get_book_by_id(1))
