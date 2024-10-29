class Author:
    def __init__(self, name: str, email: str, gender: str):
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return f"Author[name = {self.name}, email = {self.email}, gender = {self.gender}]"

class Book:
    def __init__(self, name: str, authors: list, price: float, qty: int = 0):
        self.name = name
        self.authors = authors  # authors is a list of Author objects
        self.price = price
        self.qty = qty

    def getName(self):
        return self.name

    def getAuthors(self):
        return self.authors

    def getPrice(self):
        return self.price

    def setPrice(self, price: float):
        self.price = price

    def getQty(self):
        return self.qty

    def setQty(self, qty: int):
        self.qty = qty

    def getAuthorNames(self):
        return ', '.join([author.name for author in self.authors])

    def __str__(self):
        # Tạo chuỗi authors_str bằng cách nối từng phần tử (là các đối tượng Author) của danh sách authors thành chuỗi
        authors_str = ', '.join([str(author) for author in self.authors])
        return f"Book[name = {self.name}, {{{authors_str}}}, price = {self.price}, qty = {self.qty}]"

# Test Setter and Getters of Book class
book3 = Book("Python per tutti", [Author("Charles Severance", "sev@nowhere.com", "m"),
                                  Author("Alessandro Rossetti", "sev@nowhere.com", "m"),
                                  Author("Vittore Zen", "sev@nowhere.com", "m")], 0, 100)

print(f"name: {book3.getName()}, price: {book3.getPrice()}, qty: {book3.getQty()}")
print(book3.getAuthorNames())
book3.setPrice(250)
book3.setQty(20)
print(book3)