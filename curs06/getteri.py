# class Dog:
#     nr_picioare = 4
#
#     def __init__(self, name):
#         self.name = name
#         Dog.nr_picioare -= 1
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def nume_caine(self):
#         return self.name
#
#     @staticmethod
#     def latra():
#         print(f'Ham ham latra {Dog.nr_picioare}')
#         return True


# obiect_1 = Dog('Rex')
# obiect_1.latra()
# Dog.latra()
# obiect_2 = Dog('Tom')
# print(obiect_1.name)
# print(obiect_1.nr_picioare)
# print(Dog.nr_picioare)


class Dog:
    def __init__(self, prenume):
        self.__name = prenume
    @property
    def nume_de_familie(self):
        return self.__name

    @nume_de_familie.setter
    def nume_de_familie(self, name_1):
        self.__name = name_1

    # @nume_de_familie.setter
    # def name_2(self, name_1):
    #     self.__name = name_1

    @nume_de_familie.deleter
    def nume_de_familie(self):
        del self.__name


obiect_1 = Dog("Rex")
# print(obiect_1.nume_de_familie)
# print(obiect_1.name)
# print(obiect_1.__name)
# print(obiect_1.__dict__)
# print(obiect_1._Dog__name)
# obiect_1.name = 'Tom'
# print(obiect_1.__dict__)
# print(obiect_1.name)
# print(obiect_1.name_2)
# print(obiect_1.nume_de_familie)
# obiect_1.nume_de_familie = 'Vasilica'
# obiect_1.name_2 = 'Vasilica'
# obiect_1.name = 'Popescu'
# print(obiect_1.name_2)
# print(obiect_1.name)
# print(Dog.nume_de_familie)
x = hasattr(obiect_1, 'nume_de_familie')
print(x)
# del obiect_1.name
# print(obiect_1.name)
