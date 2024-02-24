class Person:
    name = "Soikot"
    occupation = "Web Developer"
    netWorth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Shahriar"
a.occupation = "Software Developer"

b.name = "Hasan"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()