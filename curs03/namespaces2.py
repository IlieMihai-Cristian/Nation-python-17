variabila = 1


# def suma(a, b):
#     global variabila
#     variabila = a + b
#     print(variabila, 'variabila in functie')
#     def suma_2(a, b, variabila_2):
#         print(a, 'a')
#         print(b, 'b')
#         print(variabila_2, 'variabila in suma_2')
#         variabila_2 = a + b + variabila_2
#         print(variabila_2, 'variabila dupa adunare')
#         return variabila_2
#     variabila = suma_2(a, b, variabila)
#     return variabila


def suma(a, b):
    global variabila
    variabila = a + b
    print(variabila, 'variabila in functie')
    def suma_2(a, b, variabila_2):
        print(a, 'a')
        print(b, 'b')
        print(variabila_2, 'variabila in suma_2')
        variabila_2 = a + b + variabila_2
        print(variabila_2, 'variabila dupa adunare')
        return variabila_2
    variabila = suma_2(a, b, variabila)
    return variabila

print(variabila, 'variabila')
print(suma(1, 2), 'functie')
print(variabila, 'variabila dupa apelare functie')

# suma_2(1, 1, 3)
