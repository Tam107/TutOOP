class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def getName(self) -> str:
        return self.name

    def getAddress(self) -> str:
        return self.address

    def setAddress(self, address: str) -> None:
        self.address = address

    def __str__(self) -> str:
        return f"{self.name}({self.address})"


class Student(Person):
    def __init__(self, name: str, address: str, courses=None, grades=None):
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = courses if courses is not None else []
        self.grades = grades if grades is not None else []

    def addCourseGrade(self, course: str, grade: str) -> None:
        self.numCourses += 1
        self.grades.append(grade)
        self.courses.append(course)

    def printGrades(self) -> None:
        for course, grade in zip(self.courses, self.grades):
            print(f"{course}: {grade}", end=" | ")
        print()

    def getAverageGrade(self) -> float:
        if self.numCourses == 0:
            return 0
        return sum(self.grades) / self.numCourses

    def __str__(self) -> str:
        return f"{self.name}({self.address})"
# Testing the Student class as per your example
st1 = Student("Nguyen Van An", "Thai Binh")
courseGrades = [("DSA", 8), ("SS1", 9), ("SS2", 9)]

for course, grade in courseGrades:
    st1.addCourseGrade(course, grade)

st1.printGrades()
print(f"Average grade: {st1.getAverageGrade():.2f}")
