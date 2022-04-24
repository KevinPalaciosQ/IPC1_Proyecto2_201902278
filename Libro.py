class Libro():
    def __init__(self,id_book,book_title,book_type,author,book_count,book_available,book_not_available,book_year,book_editorial):
        self.id_book= id_book
        self.book_title=book_title
        self.book_type=book_type
        self.author=author
        self.book_count=book_count
        self.book_available=book_available
        self.book_not_available=book_not_available
        self.book_year=book_year
        self.book_editorial=book_editorial
    
    def getid_book(self):
        return self.id_book
    
    def getbook_title(self):
        return self.book_title

    def getbook_type(self):
        return self.book_type
    
    def getauthor(self):
        return self.author

    def getbook_count(self):
        return self.book_count
    
    def getbook_available(self):
        return self.book_available

    def getbook_not_available(self):
        return self.book_not_available

    def getbook_year(self):
        return self.book_year   

    def getbook_editorial(self):
        return self.book_editorial

    def setid_book(self, id_book):
        self.id_book=id_book    
    
    def setbook_title(self, book_title):
        self.book_title=book_title
    
    def setbook_type(self, book_type):
        self.book_type=book_type

    def setauthor(self, author):
        self.author=author

    def setbook_count(self, book_count):
        self.book_count=book_count

    def setbook_available(self, book_available):
        self.book_available=book_available

    def setbook_not_available(self, book_not_available):
        self.book_not_available=book_not_available

    def setbook_book_year(self, book_year):
        self.book_year=book_year

    def setbook_editorial(self, book_editorial):
        self.book_editorial=book_editorial