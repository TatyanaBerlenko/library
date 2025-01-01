import unittest
import requests


class TestBookAPI(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:8080'

    def setUp(self):
        self.sample_book = {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "genre": "Dystopian"
        }

    def test_get_home(self):
        """Test home page"""
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Guest', response.text)

    def test_get_all_books(self):
        """Test getting all books"""
        response = requests.get(f"{self.BASE_URL}/books")
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_valid_id(self):
        """Test getting book by valid ID"""
        response = requests.get(f"{self.BASE_URL}/books/1")
        self.assertEqual(response.status_code, 200)
        book_data = response.json()
        self.assertIsInstance(book_data, dict)
        self.assertTrue(all(key in book_data for key in ['title', 'author', 'year', 'genre']))

    def test_get_book_by_invalid_id(self):
        """Test getting book by invalid ID"""
        response = requests.get(f"{self.BASE_URL}/books/999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'The book id is invalid')

    def test_add_book_not_implemented(self):
        """Test adding a new book (currently not implemented)"""
        response = requests.post(f"{self.BASE_URL}/books", json=self.sample_book)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_error_handling(self):
        """Test error handling"""
        # Test with invalid JSON
        response = requests.post(f"{self.BASE_URL}/books", data='invalid json')
        self.assertEqual(response.status_code, 405)

        # Test with missing required fields
        invalid_book = {"title": "Test Book"}
        response = requests.post(f"{self.BASE_URL}/books", json=invalid_book)
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()