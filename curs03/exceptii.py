# variabila, impartire = 1, None

try:
    print(variabila)
    a = int(input('Prima valoare: '))
    b = int(input('A doua valoare: '))
    impartire = a / b

    valoare_utilizator = int(input("Adauga o litera: "))
    print(valoare_utilizator)
except ValueError:
    print('eroare de valoare, te rugam sa introduci o litera')
    while (valoare_utilizator := input("Adauga o litera: ")) and valoare_utilizator.isdigit() is False:
        continue
    print(valoare_utilizator)
except NameError as e:
    # variabila = None
    print(e)
except ZeroDivisionError:
    print('impartirea la zero nu e permisa', b)
    while b == 0:
        b = int(input('A doua valoare: '))
    impartire = a / b
except Exception as e:
    print(e)
else:
    print('a functionat fara probleme')
finally:
    print('aici inchidem fisierul')


