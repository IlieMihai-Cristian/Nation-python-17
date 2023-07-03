my_dict = {1: 'car', 2: 'bike'}

dictionar = {}
for num in range(1, 11):
    dictionar[num] = num * num
print(dictionar)

dictionar = {num: num * num for num in range(1, 11)}
print(dictionar)
