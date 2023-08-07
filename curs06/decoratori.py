
# def decorator_simplu(functie_decorata):
#     print(f"Apelam functia {functie_decorata.__name__}")
#     return True
#
#
# @decorator_simplu
# def functie_simpla():
#     return 'Buna seara'
#
#
# @decorator_simplu
# def functie_complexa():
#     return 'Noapte buna'


# print(functie_simpla())


# def decorator_depozite(functie_decorata):
#     def ambalaj_metoda(parametru_functie):
#         return f"Ambalam produse din {functie_decorata.__name__} care contine cartea {parametru_functie}"
#     return ambalaj_metoda
#
#
# @decorator_depozite
# def impachetare_carti(nume):
#     return nume
#
#
# print(impachetare_carti('Ion'))
# print(impachetare_carti('Baltagul'))

# def decorator_depozit(material):
#     def ambalaj(functie_decorata):
#         def ambalaj_intern(*carte):
#             return f"Ambalaj produse din {functie_decorata.__name__} cu material {material} care contine cartile {', '.join(carte)}"
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*nume):
#     return nume
#
#
# print(impachetare_carti("Baltagul", "Ion"))
import time
#
# def calculeaza_timpul(functie_decorata):
#     def functie_interioara(*param):
#         inceput = time.time()
#         suma = functie_decorata(*param)
#         sfarsit = time.time()
#         print(f"Timp total de executie: {sfarsit - inceput}")
#         return suma
#     return functie_interioara
#
#
# @calculeaza_timpul
# def adunare(*args):
#     suma = 0
#     for i in args:
#         suma += i
#     return suma
#
#
# print(adunare(1, 2, 3))


def calculeaza_timpul(functia_decorata):
    def functie_interioara(param):
        inceput = time.time()
        suma = functia_decorata(param)
        sfarsit = time.time()
        print(f"Timp total de executie: {sfarsit - inceput}")
        return suma
    return functie_interioara


@calculeaza_timpul
def adunare(number):
    suma = 0
    for i in range(number):
        suma += i
    return suma


print(adunare(100000000))
