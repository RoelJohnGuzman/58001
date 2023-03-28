class Person:
    def __init__(self, name, pre, mid, fin):
        self.__name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin
        self.__avg = (self.__pre + self.__mid + self.__fin) / 3

    def Grade(self):
        print("Name:", self.__name)
        print("The average is", self.__avg)


class Student1(Person):
    pass


class Student2(Person):
    pass


class Student3(Person):
    pass


std1 = Student1("Despi", 100, 80, 99)
std1.Grade()
std2 = Student2("Omen", 97, 90, 95)
std2.Grade()
std3 = Student3("Host", 90, 92, 96)
std3.Grade()
