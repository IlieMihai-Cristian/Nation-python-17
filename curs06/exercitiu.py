"""
Vehicule -> clasa generica
    1. Apa
    2. Aer (avioane)
    3. Spatiu
    4. Terestru
    Proprietati comune:
    - motor
    - roti
    - transport
"""
"""
Max este un pisica mare care doarme toata ziua.
nume obiect: Max
denumire clasa: pisica
proprietate: mare
activitate: doarme toata ziua


O masina Dacia rosie merge incet.
nume obiect: Dacia
denumire clasa: masina
proprietate: rosie
activitate: merge
"""
"""
LIFO - Last In First Out
FIFO - First In First Out
"""
stiva = []


def push(val):
    stiva.append(val)


def pop():
    val = stiva[-1]
    del stiva[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
