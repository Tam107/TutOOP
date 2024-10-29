from dataclasses import dataclass

@dataclass
class Author:
    name: str
    email: str
    gender: str  # should be 'm' or 'f'

    def getName(self) -> str:
        return self.name

    def getEmail(self) -> str:
        return self.email

    def setEmail(self, email: str) -> None:
        self.email = email

    def getGender(self) -> str:
        return self.gender

    def __str__(self) -> str:
        return f"Author[name = {self.name}, email = {self.email}, gender = {self.gender}]"


@dataclass
class Book:
    name: str
    author: Author  # Author instance
    price: float
    qty: int = 0  # default value is 0

    def getName(self) -> str:
        return self.name

    def getAuthor(self) -> Author:
        return self.author

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, price: float) -> None:
        self.price = price

    def getQty(self) -> int:
        return self.qty

    def setQty(self, qty: int) -> None:
        self.qty = qty

    def __str__(self) -> str:
        return f"Book[name = {self.name}, {self.author}, price = {self.price}, qty = {self.qty}]"
