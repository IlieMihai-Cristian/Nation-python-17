list_1 = [1, 5, 4, 6, 8, 11, 3, 12]

# list_3 = list(map(lambda x: x*2, list_1))
# print(list_3)


# def iterare(x):
#     lista_noua = []
#     for i in x:
#         lista_noua.append(i*2)
#     return lista_noua
#
#
# print(iterare(list_1))

def suma(n):
    return n + n


numere = (1, 2, 3, 4)
rezultat = map(lambda x: x + x, numere)
# rezultat = map(suma, numere)
print(list(rezultat))
