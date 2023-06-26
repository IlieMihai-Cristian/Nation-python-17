# print("Afisare mesaj din functii.py")
# var1 = 1
# "String {}".format(var1)
# input("Adauga o cifra: ")

# var_1 = 4
#
#
# def functie_suma(param_0, param_1: int = var_1, param_2: int = 3) -> (str, str):
#     """
#     :param param_1: primul parametru
#     :param param_2: al doilea parametru
#     :return: suma si diferenta celor doi param
#     """
#     print(param_1, 'param1')
#     return param_1 + param_2, param_1 - param_2
#     # print("nu se executa")
#
#
# # suma, diferenta = functie_suma(2, 3)
# # suma, diferenta = functie_suma(7, param_2=5)
# suma, diferenta = functie_suma(param_2=5, param_0=7)
#
# print(suma, 'suma')
# print(diferenta, 'diferenta')


def suma(a, b, c, *lista_studenti, **kwargs):
    print(kwargs)
    total = a + b + c
    for i in lista_studenti:
        total += i
    for j in kwargs.values():
        total += j
    return total


# print(suma(1, 2, 3))
# print(suma(a=1, b=2, c=3))
# print(suma(b=2, a=1, c=3))
# print(suma(3, b=2, a=1))
# print(suma(1, 2, 3, (4, 5, 6)))
# print(suma(a=1, b=2, c=3, args=(4, 5, 6)))
print(suma(4, 5, 6, 5, 6, 7, d=7, e=8, f=9))

