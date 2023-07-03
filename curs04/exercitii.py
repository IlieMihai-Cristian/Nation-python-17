# lista = []
# for i in range(10):
#     if i % 2 == 0:
#         lista.append('par')
#     else:
#         lista.append('impar')
#
# print(lista)
# lista = ['par' if i % 2 == 0 else 'impar' for i in range(10)]
# print(lista)

# lista = []
# for i in ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']:
#     if i == 'sambata' or i == 'duminica':
#         lista.append('weekend')
#     else:
#         lista.append('zi lucratoare')
# print(lista)

# lista = ['weekend' if i == 'sambata' or i == 'duminica' else 'zi lucratoare' for i in ['luni', 'marti', 'miercuri',
#                                                                                        'joi', 'vineri', 'sambata',
#                                                                                        'duminica']]
# print(lista)

# 2
# dictionar = {}
# for i, v in enumerate(['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']):
#     if i > 4:
#         dictionar[v] = 'weekend'
#     else:
#         dictionar[v] = 'zi lucratoare'
# print(dictionar)
#
# dictionar = {v: 'weekend' if i > 4 else 'zi lucratoare' for i, v in enumerate(['luni', 'marti', 'miercuri', 'joi',
#                                                                                'vineri', 'sambata', 'duminica'])}
# print(dictionar)

# 3

persoane = [{
    'name': 'Alice',
    'age': 23,
},
    {
        'name': 'Ana',
        'age': 31
    },
    {
        'name': 'Ion',
        'age': 12
    }]
#
# date_angajati = {}
# for i in persoane:
#     if i['age'] > 22:
#         date_angajati[i['name']] = i['age']
# print(date_angajati)
#
# # date_angajati = {i['name']: i['age'] for i in persoane if i['age'] > 22}
# date_angajati = {i['name']: i['age'] if i['age'] > 22 else '-' for i in persoane }
# print(date_angajati)

#4
# set_date_angajati = set()
# for i in persoane:
#     if i['age'] > 22:
#         set_date_angajati.add(i['name'])
# print(set_date_angajati)

# set_date_angajati = {i['name'] for i in persoane if i['age'] > 22}
# print(set_date_angajati)

# 5
lista = []
for x in range(50):
    if x % 2 == 0:
        if x % 5 == 0:
            lista.append(x)
print(lista)

# lista = [x for x in range(50) if x % 2 == 0 and x % 5 == 0]
lista = [x for x in range(50) if x % 2 == 0 if x % 5 == 0]
print(lista)
