variabila = 1


def suma(parametru_1):
    # global variabila
    # print(variabila)
    variabila = 2
    print(variabila)
    return "Returneaza"


print(variabila, 'variabila')
suma("orice")
print(variabila, 'dupa functie')
