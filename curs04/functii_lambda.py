# def suma(x, y):
#     return x + y


# suma(1, 2)

# suma = lambda x, y: x + y
# print(suma(1, 2))

jucatori = [{
    "first_name": "ion",
    "last_name": "vasile",
    "age": 20
},
    {
        "first_name": "ionut",
        "last_name": "barbu",
        "age": 23
    },
    {
        "first_name": "elena",
        "last_name": "tudora",
        "age": 12
    },
]
sorted_players = sorted(jucatori, key=lambda jucator: jucator["last_name"])
print(sorted_players)
