class Book:
    total_books = 0

    @classmethod
    def get_total_books(cls):
        cls.total_books += 1

Book.get_total_books()
Book.get_total_books()
Book.get_total_books()
Book.get_total_books()
print(Book.total_books)