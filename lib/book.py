class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages  # This will call the setter method
        self.read = False  # Indicates if the book has been read

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")  # Ensure this matches the test exactly
            raise ValueError("page_count must be an integer")
        self._pages = value

    def mark_as_read(self):
        self.read = True

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"{self.title}, {self.pages} pages. Read: {self.read}"