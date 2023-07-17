# grila 1
# my_numbers = {2, 5, 3, 5, 4, 1, 2}
# doubled = len(my_numbers) * 2
# print(doubled)


# grila 2
# var_1 = [x for x in range(20) if x / 2 == 0]
# print(var_1)


# grila 3
# char = 'cha'
# cha = 'char'
# print(len(char) * 'cha')


# # grila 4
# var = 1
# while var < 4:
#     for var in range(4):
#         if var == 1:
#             var += 1
#             break
#         print('var = 4')
#     var += 1
# print(var + 1)


# grila 5
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 3
# print(len(t2))

# grila 6
# def functie1():
#     print('Variabila este definita?', var)
#
#
# var = 30
# print(functie1())
# print(var)


# grila 7
# x = 10
# while x > 1:
#     x -= 1
#     continue
# print(x)


# grila 8
# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]


# lista = [1, 2, 3]
# print(functie(lista))

# string = 'alfabet'
# string = input('Alege un sir: ')
# while len(string) >= 10:
#     string = input('String prea mare, reintrodu stringul: ')
# vocale = list('aeiou')
#
#
# def nr_vocale_functie(cuvant):
#     nr_vocale = 0
#     for i in cuvant.lower():
#         if i in vocale:
#             nr_vocale += 1
#     return nr_vocale


# print(nr_vocale_functie(string))

def main():
    try:
        number = int(input("Introdu numar chei: "))
        if number not in range(1, 21):
            raise ValueError
        dictionar = {}
        for i in range(1, number + 1):
            dictionar[i] = i ** 2
        return dictionar
    except ValueError as err:
        return main()


var = main()
print(var)

def citire():
    try:
        a = int(input('Prim: '))
        b = int(input('Doi: '))
        c = int(input('Trei: '))
        return a, b, c
    except ValueError:
        print('Un numar este gresit, mai incearca o data')
        citire()


def impartire():
    a, b, c = citire()
    if b == 0 or c == 0:
        return 0
    elif a == b == c:
        return a / b / c * 3
    return a / b / c
print(impartire())


lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = list()
for j in lista:
    if j % 2 == 0:
        lista2.append(j)
        lista2.append(j * 2)
    else:
        lista2.append(j)
print(lista2)


list_example = [1, 1, 2, 3, 4, 4, 5, 1]
first_list_length = 3
result = ([1, 1, 2], [3, 4, 4, 5, 1])
def separare(lista, nr):
    lista_prim = lista[:nr]
    lista_doi = lista[nr:]
    return lista_prim, lista_doi
print(separare(list_example, first_list_length))
