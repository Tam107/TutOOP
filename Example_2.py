class Author:
    def __init__(self, name, email, gender = 'm'):
        self._name = name
        self._email = email
        if gender in ('m', 'f'):
            self._gender = gender
        else:
            raise ValueError("Gender must be 'm' or 'f'")

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getGender(self):
        return self._gender

    def setEmail(self, email):
        self._email = email

    def __str__(self):
        return f"Author[name = {self._name}, email = {self._email}, gender = {self._gender}]"


class Book:
    def __init__(self, name, author, price, qty=0):
        self._name = name
        self._author = author
        self._price = price
        self._qty = qty

    def getName(self):
        return self._name

    def getAuthor(self):
        return self._author

    def getPrice(self):
        return self._price

    def getQty(self):
        return self._qty

    def setPrice(self,price):
        self._price = price

    def setQty(self,qty):
        return self._qty

    def __str__(self):
        return f"Book[name = {self._name},author {self._author}, price = {self._price}, qty = {self._qty}]"

if __name__ == "__main__":
    kathySierra = Author("Kathy Sierra", "sierra@nowhere.com", "f")
    print(f"name: {kathySierra.getName()}, email: {kathySierra.getEmail()}, gender: {kathySierra.getGender()}")
    kathySierra.setEmail("sierra@somewhere.net")
    print(kathySierra)
    paulBarry = Author("Paul Barry", "barry@nowhere.com", "m")
    kathySierra.setEmail("sierra@somewhere.net")