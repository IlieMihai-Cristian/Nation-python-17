# class A:
#     pass
#     # def info(self):
#     #     print('Class A')
#
# class F:
#     def info(self):
#         print('class F')
# class B(A, F):
#
#     pass
#     # def info(self):
#     #     print('Class B')
# class E:
#     def info(self):
#         print('Class e')
#
#
# class C(E):
#     pass
#     # def info(self):
#     #     print("Class C")
# class D(E, C):
#     pass
#     # def info(self):
#     #     print("Class D")
#
# D().info()


# class Example:
#
#     def __init__(self, val=1):
#         self.first = val
#
#     def set_second(self, valoare):
#         return valoare
#
#
# obj_1 = Example()
# print(obj_1.set_second(4))
# print(obj_1.set_second(2))
# print(obj_1.__dict__)
#
# obj_2 = Example(2)
# print(obj_2.__dict__)
#
# obj_2.third = 5
# print(obj_2.__dict__)



# class Example:
#
#     def __init__(self, val=1):
#         self.__first = val
#         # cu underscore in fata este protejata
#         # cu dublu underscore in fata este privata
#
#     def set_second(self, valoare):
#         return valoare
#
#
# obj_1 = Example()
# print(obj_1)
# print(obj_1.set_second(4))
# print(obj_1.__dict__)
#
# # print(obj_1.first, 'prop')
# print(obj_1._Example__first, 'prop')
# # print(obj_1.__dir__())
#
# var = '123'
# print(var.__dir__())


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         # Example.__counter += 1
#         self.__counter += 1
#
# object_1 = Example()
# object_2 = Example()
# object_3 = Example()
#
# print(object_1._Example__counter)
# print(object_2._Example__counter)
# print(object_3._Example__counter)


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#             Example.a = 5
#         else:
#             self.b = 2
#
#
# obj_1 = Example()
# print(getattr(obj_1, 'a', None))


# class Vehicule:
#     pass
#
# class Masini(Vehicule):
#     pass
#
# class MasiniDeTeren(Masini):
#     pass
#
#
# # print(issubclass(MasiniDeTeren, Vehicule))
# # print(issubclass(Vehicule, MasiniDeTeren))
#
# vehicul_1 = Vehicule()
# masina_1 = Masini()
# masina_de_teren = MasiniDeTeren()
# print(isinstance(masina_1, Masini))
# print(isinstance(masina_1, MasiniDeTeren))
# print(isinstance(masina_1, Vehicule))


class ClassTest:
    sub_variabila = 'test'

class SuperClasa(ClassTest):
    super_variabila = 'super'
    # sub_variabila = 'sub_parinte'

    def __init__(self, name='Mihai'):
        self.name = name
        self.var_init = 30

    # def __str__(self):
    #     return f'Numele meu este {self.name}'


class Mijloc:

    variabila_mijloc = 3
    super_variabila = 'mijloc'
    sub_variabila = 'sub'


class SubClasa(SuperClasa, Mijloc):

    # sub_variabila = 'sub'
    super_variabila = 'super_copil'

    def __init__(self, name='Cristian'):
        super().__init__(name)
        self.var_init = 12

    # def __str__(self):
    #     return f'Print {self.name}'


# object_1 = SubClasa()
# # print(object_1)
# print(object_1.var_init)

object_2 = SubClasa('George')
print(object_2.sub_variabila)
