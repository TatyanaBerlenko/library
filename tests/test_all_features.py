import requests

BASE_URL = "http://localhost:8080"


def test_home_page():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200, "Home page did not return status code 200"


def test_guest_page():
    response = requests.get(f"{BASE_URL}/Guest")
    assert response.status_code == 200, "Guest page did not return status code 200"


def test_books_page():
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200, "Books page did not return status code 200"


def test_add_book_page():
    response = requests.get(f"{BASE_URL}/books/add")
    assert response.status_code == 200, "Add book page did not return status code 200"


def test_edit_book_page():
    response = requests.get(f"{BASE_URL}/books/edit/1")
    assert response.status_code in [200, 404], "Edit book page returned an unexpected status code"
