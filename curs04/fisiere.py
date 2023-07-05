"""
r -> citim, nu adaugam, este valoarea default cu care vine functia open, daca fisierul nu exista, apare eroare
w -> scriere, daca fisierul nu exista, il adauga, daca ceva in fisier, se rescrie
a -> scriere, daca exista ceva in fisier, adauga
r+ -> scriere, citire, daca fisierul nu exista, apare eroare
"""

# file = open("data.txt", "w")
# file = open("data.txt", "a")
# file = open("data1.txt", "r+")
# file.write("hello1")
# file.close()
# scriere
with open("data.txt", "w") as file:
    file.write('Hello\n')
    file.write('Hello\n')


# citirea liniilor in acelasi timp
#
# with open("data.txt", "r") as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)

# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#
#         if not line:
#             break
#         print(line)

import csv


# with open('fisiercsv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     for index, row in enumerate(rows):
#         print(row)
#         if index > 0:
#             if index == 1:
#                 min_cp, max_cp = int(row[3]), int(row[3])
#                 continue
#             # else:
#             if int(row[3]) < int(min_cp):
#                 min_cp = int(row[3])
#             if int(row[3]) > int(max_cp):
#                 max_cp = int(row[3])
#     print(min_cp, max_cp)

# new_cars = [
#     ['Dacia', 'Logan', 2005, 75],
#     ['Renault', 'Clio', 2005, 75]
# ]
# with open('data_csv.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for new_car in new_cars:
#         csv_writer.writerow(new_car)

# def csv_reader():
#     lista_elemente = []
#     with open('categorii.csv','r+') as file:
#         categori = csv.reader(file)
#         for item in categori:
#             lista_elemente.append(item)
#     return lista_elemente
#
#
# with open('categorii.csv', mode='a', newline='') as file:
#     lista_elemente = csv_reader()
#     print(lista_elemente)
#     variabila_categorie = input("Adauga un nou element: ").lower()
#     lista_elemente_noi = [i[0].lower() for i in lista_elemente]
#     if variabila_categorie not in lista_elemente_noi:
#         writer = csv.writer(file)
#         writer.writerow([variabila_categorie])
#     else:
#         print('elementul deja exista')


import datetime


def verificare(an, luna, zi):
    try:
        datetime.datetime(int(an), int(luna), int(zi))
        return True
    except ValueError:
        return False


print(verificare(23, 2, 28))
