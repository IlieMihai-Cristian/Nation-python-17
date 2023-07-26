class Super:
    def __init__(self, name='Ioana'):
        self.name = name
    def inaltime(self):
        return 180
    def __str__(self):
        return f"Numele meu este {self.name}"


class Sub(Super):
    # def __init__(self, name='Rebeca', age=56):
    #     super().__init__(name)

    # def inaltime(self):
    #     return 190

    def __str__(self):
        return "George"


# obiect_2 = Super("Ioana")
# print(obiect_2)
# obiect_1 = Sub("Alexandra1", 17)
obiect_1 = Sub().inaltime()
print(obiect_1)
