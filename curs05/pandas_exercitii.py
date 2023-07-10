import pandas as pd

# a = [1, 7, 2]
# variabila = pd.Series(a, index=['x', 'y', 'z'])
# print(variabila[1])
# print(variabila['y'])

# taskuri = {"ziua1": 2, "ziua2": 4, "ziua3": 1}
# variabila = pd.Series(taskuri, index=['ziua2', 'ziua3'])
# print(variabila)

taskuri = {
    "zile": [2, 4, 5],
    "durata": [50, 40, 45]
}
variabila = pd.DataFrame(taskuri)
print(variabila)
