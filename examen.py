# 1
# x = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "a": 4,
#     "d": 5
# }
# print(x['a'])
"""
a. The code will throw an error because we cannot have duplicate keys in dictionaries.
b. 1
c. 4 (Correct)
d. None of the above options is correct.
"""

# 2
# x = list(range(1, 20))
# print(x)
# x = [i for i in x if i % 2 == 0]
# print(x)
"""
a. [2, 4, 6, 8. 10, 12, 14, 16, 18] (corect)
b. [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
c. None of the above options is correct.
"""

# 3
"""
Which of the following is invalid?

Select one:
a. __a = 1
b. none of the mentioned (corect)
c. _a = 1
d. __str__ = 1
"""
# __a = 1
# print(__a)
# __str__ = 1
# print(__str__)
# _a = 1
# print(_a)


# 4
# def a(d):
#     # c = {}
#     d[4] = 'd'
#     # c.update({4: 'd'})
#     # return c
#     return d
#
# x = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
#
# y = a(x)
# print(x is y)
"""
a. True
b. False
"""

# 5

#
# class Clasa:
#     def __init__(self):
#         self.s = "suc"
#     def metoda1(self):
#         print(self.s)
#         self.s = 'test'
#
#     def metoda2(self):
#         print(self.s.upper())
# strobj = Clasa()
# strobj.metoda1()
# strobj.metoda2()
# strobj.metoda1()
# strobj.metoda2()
"""
a. Error
b. test
c. None
d. TEST (corect)
"""


# 6
# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]
#
#
# lista = [1, 2, 3]
# print(functie(lista))
"""
a. 3
b. 6
c. None
d. Error
"""

# 7
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 3
#
# print(len(t2))
"""
a. 3
b. 9
c. Error
d. (1, 10, 100, 1, 10, 100, 1, 10, 100)
"""

# 8


# def functie1():
#     # global var
#     # var = 20
#     print("Variabila este definita?", var)
#
#
# var = 30
# functie1()
# print(var)
"""
a. Variabila este definita?
b. Variabila este definita? 30
30 (corect)
c. Error
d. Variabila este definita? 30
"""
# 9

# x = 10
# while x > 1:
#     x -= 1
#     continue
#     # break
# print(x)
"""
a.
Infinite loop
b. 9
8
7
6
5
4
3
2
1 
c. x = [1, 2, 3]
d. 1 (corect)
"""


# 10
# my_var = ['a', 'b', {'x': 1, 'z': {'key': 30, 'w': 2}}, {'a': 30, "b": 40}, 10]
# print(my_var[2]['z']['key'])
"""
Select one:
a. my_var[2]['z']['key'] (corect)
b. my_var['key']
c. my_var[2]['key']
"""
# for i in my_var:
#     if type(i) == dict:
#         for v in i.values():
#             if type(v) == dict:
#                 for a, b in v.items():
#                     if b == 30:
#                         print(a, b)
# api = [{"client": 'Ana', "nr_contract": 1},
#        {"client": "Maria", "nr_contract": 2},
#        {"client": "Ana", "nr_contract": 4}]

# api = [{"client": 'Ana', "nr_contract": [1, 4]},
#        {"client": "Maria", "nr_contract": 2}]
# api = [{"client": 'Ana', "nr_contract": [{"contract1": 1}, {"contract2": 4}]},
#        {"client": "Maria", "nr_contract": 2}]

# 11

# x = ["ab", "cd", "ed"]
# for i, v in enumerate(x):
#     # i.title()
#     x[i] = v.title()
# print(x)
"""
a. ['ab', 'cd', 'ed'] (corect)
b. none of the mentioned
c. ['Ab', 'cd', 'ed']
d. [‘Ab’, ‘Cd’, 'Ed']
"""

# 12
# i = 2
# while True:
#     if i // 3:
#         break
#     print(i)
#     i += 3
"""
a. error
b. 2 (corect)
c. Infinite loop
d. 2 4 6 8 10 …
"""

# 13
# try:
#     i = int("Hello")
# except Exception as e:
#     print(e)
"""
a. Eroare (corect)
b. None
c. Hello!
d. “Hello!”
"""

# 14
# test_dict = {"element1": 1, "element2": 3, "element3": 2}
# res = list(test_dict.keys()) + list(test_dict.values())
# print(str(res))
"""
a. ['element1', 'element2', 'element3']
b.
c. 'element1', 'element2', 'element3'
d.['element1', 'element2', 'element3', 1, 3, 2] (corect)
e. [1, 3, 2]
"""

# 15
# cuvant = "cu'va\\'nt"
# cuvant = "cu'va\"nt"
# print(cuvant)
# print(cuvant[::-1])
"""
a. cuvant
b. [“t”, “n”, "'", "\", "\",  “a”, “v”, "'", “u”, “c”]
c. tn'\\av'uc
d. tn'\av'uc (corect)
"""
# 16
# def functie():
#     l = list()
#     for i in range(1, 3):
#         l.append(i**2)
#     print(l)
#
# functie()
"""
a. [1, 4] (corect)
b. []
c. [1, 9]
d. [0, 1, 2, 3]
"""
# 17


# def functie1(n):
#     if n % 2 == 0:
#         print(True)
#
#
# print(functie1(2))
"""
a. True
None (corect)
b. Error
c. None
d. True
"""

# 18
# class Clasa:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
#
# obiect = Clasa(1)
# print(obiect.a)
# print(obiect.b)
"""
a. 1 (corect)
b. None
c. 2
d. Error
"""


# 19

# class Clasa:
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#
#     def __str__(self):
#         return f"{self.nume} - {self.prenume}"
#
#
# student = Clasa("Ion", "Popescu")
# print(student)
"""
a. Ion Popescu
b. Eroare
c. “Ion” “Popescu”
d. Ion – Popescu (corect)
"""

# 20

# class SuperClasa:
#     def __init__(self, name):
#         self.nume = name
#
#     def __str__(self):
#         return "Numele meu este " + self.nume + "."
# class SubClasa(SuperClasa):
#     def __init__(self, name):
#         # SuperClasa.__init__(self, name)
#         super(SubClasa, self).__init__(name)
#
#     # def __str__(self):
#     #     return "Ana are mere"
#
# obj = SubClasa("Alexandra")
# print(obj)
"""
a. Numele meu este self.nume.
b. Eroare
c. None
d. Numele meu este Alexandra.
"""

# 21
# class SuperClasa:
#     supVar = 1
#
# class SubClasa(SuperClasa):
#     subVar = 2
#
# obj = SubClasa()
# print(obj.supVar)

"""
a. None
b. 2
c. 1 (corect)
d. Eroare
"""

# 22
# class SuperClasa:
#     def __init__(self):
#         self.supVar = 11

# class SubClasa(SuperClasa):
#     def __init__(self):
#         # self.supVar = 12
#         super().__init__()
#         print(self.supVar)
#         # super().__init__()
#
# obj = SubClasa()
# print(obj.supVar)

"""
a. 12
b. Eroare (eroare)
c. 11
d. None
"""
# 23
# class A:
#     a1 = 10
#
#     def __init__(self, a1):
#         A.a1 = a1
#
# obj1 = A(20)
# print(obj1.a1)
# obj2 = A(30)
# print(obj1.a1)

"""
a. 10
b. 30
c. None of the other options.
d. 20
"""
# 24
# x = []
# i = 0
# while True:
#     if len(x) >= 10:
#         break
#     i += 1
#     if i % 2 == 1:
#         continue
#     x.append(i)
# print(x)
"""
a. The code will result in an infinite loop because the condition in while is always True.
b. 2, 4, 6, 8, 10
c. 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 (corect)
d. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
e. None of the above options is correct.
"""
# 25
# class A:
#     a1 = 10
# class B(A):
#     def __init__(self, a1):
#         self.a1 = a1
#         A.a1 = a1 * 2
#
# class C(A):
#     pass
#
# obj1 = A()
# obj2 = B(20)
# obj3 = C()
# print(obj1.a1, obj2.a1, obj3.a1)
"""
a. 10 10 10
b. 40 20 40 (corect)
c. 10 40 40
d. 10 20 40
"""
# 26
# class A:
#     x = "A"
#     def func(self):
#         return self.x
#
# class B(A):
#     x = "B"
# aObj = A()
# bObj = B()
# print(aObj.func(), bObj.func())
"""
a. 'B' object has no attribute 'func'
b. A B (corect)
c. A A
"""

# 27
# x = {
#     1: "a",
#     2: "b",
#     3: "c"
# }
# y = x.get(4, 'd')
# print(y)
"""
a.The code will throw an error because method get is not available for dictionaries.
b. The code will output d because we're using the get method. Since the key 4 is not present in the dictionary, 
variable y will be assigned with value d passed as the second attribute of the get method (fallback value if the key is 
not present in the dictionary). (corect)
c. The code will output None because the key with value 4 is not present in the dictionary,
d.The code will throw an error because we're trying the access key with value 4 which does not exists in the 
dictionary x.
e. The code will output d because we're setting a new key with value 4 and value d in the dictionary and then we assign 
this new value to variable y.
"""
# 28
# my_list = [1, 2, 3]
# try:
#     x = my_list[3]
# except IndexError:
#     msg = "Indexul nu a fost gasit"
# except NameError:
#     msg = "Variabila nu a fost definita!"
# finally:
#     msg = "Totul a mers perfect"
# print(msg)
"""
Select one:
a. 'Totul a mers perfect' (corect)
b. 'Variabila nu a fost definita!'
c. 'Indexul nu a fost gasit!'
"""
# 29
# dictionar = {"pisica": "pisica1", "caine": "caine1", "cal": "cal1"}
# dictionar['pisica'] = "pisica2"
# print(dictionar)
"""
a. {'pisica': 'pisica2', 'caine': 'caine1', 'cal': 'cal1'} (Corect)
b. [‘pisica2’, ‘caine1’, ‘cal1’]
c. [‘pisica’, ‘caine’, ‘cal’]
d. {‘pisica’: ‘pisica1’, ‘caine’: ‘caine1’, ‘cal’: ‘cal1’}
"""
# 30
class Joc:
    def __init__(self):
        self.name = "john"

class Jucator(Joc):
    def __init__(self):
        self.name = "ss"
        super().__init__()

obj = Jucator()
print(obj.name)

"""
a. John (corect)
b. ss
c. error
"""
