class Book:
    """A class representing a book with title, author, and checkout status."""

    def __init__(self, title: str, author: str):
        """
        Initialize a Book instance.

        :param title: The title of the book
        :param author: The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Was already available


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book: Book):
        """Add a Book instance to the library collection."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return  # Successfully checked out
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title: str):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return  # Successfully returned
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print all books that are currently available (not checked out)."""
        available_books = [book for book in self._books if not book._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")