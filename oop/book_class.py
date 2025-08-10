class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Called when the instance is about to be destroyed
        print(f"Deleting {self.title}")

    def __str__(self):
        # Informal / nicely readable string
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation that can be used to recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
