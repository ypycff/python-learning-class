class Person:

    name = ""
    age = -1

    def __init__(self, name, age):
        self.name = name
        self.age = age
		
    def __str__(self):
        return "{0}, {1}".format(self.name, self.age)

p1 = Person("John", 21)
print(type(p1))