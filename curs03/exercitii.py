# 1
# x = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'a': 4,
#     'd': 5
# }
# print(x['a'])

# 2
# def a(parametru):
#     parametru[2] = 'f'
#     return parametru
#
#
# x = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
#
# y = a(x)
# print(y)


# 3
# def functie1(lista_cuvinte):
#     lista = []
#     for n in lista_cuvinte:
#         lista.append((len(n), n))
        # return lista
    # return lista[-1][0], lista[-1][1]
    # print('print')
    # lista.sort()



# rezultat, rezultat1 = functie1(['pip', 'Exercitiu', 'Python'])
# rezultat = functie1(['pip', 'Exercitiu', 'Python'])
# print(rezultat)
# print(rezultat1)

# 4


# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]
#
#
# lista = [1, 2, 3]
# print(functie(lista))


# 5
#
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 4
# print(t2)
# print(len(t2))


# 6

# def functie1():
#     # print("Variabila este definita", var)
#     return f"Variabila este definita {var}"
#
#
# var = 30
# print(functie1())
# print(var)


# 7

# x = 10
# while x > 1:
#     x -= 1
#     continue
#
# print(x)


# 8

# x = ['ab', 'cd', 'ed']
# for i, j in enumerate(x):
#      x[i] = j.title()
#
# print(x)


# 9

# lista1 = list(set([1, 3, 4, 3, 5, 6]))
# lista1 = set([1, 3, 4, 3, 5, 6, 7, 8, 7])
# print(lista1)
# lista1 = list(lista1)
# print(lista1)
# del lista1[0:5]
# print(lista1)


# 10
# cuvant = "cu'va\\'nt"
# cuvant = "cu'va\"nt"
# print(cuvant)
# print(cuvant[::-1])


# 11

# def functie():
#     l = list() # l = []
#     # for i in range(1, 4, 2):
#     for i in range(1, 4, 2):
#         l.append(i**2)
#     print(l)
#
# functie()


# 12
# def a(*args):
#     return args
#
#
# s = a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(s)

# 13
# a = {1: 'a', 2: 'b', 3: 'c'}
# b = {2: 'd', 3: 'e', 4: 'f'}
# print({**a})
# c = {**a, **b}
# print(c)


#14
# dictionar = {"pisica": "pisica1", "caine": "caine1", "cal": "cal1"}
dictionar = {"caine": "caine1", "cal": "cal1"}
dictionar['pisica'] = 'pisica2'
print(dictionar)
