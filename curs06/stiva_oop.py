class Stiva:
    valoare = 0

    def __init__(self, *val):
        self.stiva = []
        self.val = val
        self.alegere = input('Alege intre 1 si 2: ')

    def push(self):
        for i in self.val:
            self.stiva.append(i)

    def pop(self):
        val = self.stiva[-1]
        del self.stiva[-1]
        return val

    def __str__(self):
        if self.alegere == '1':
            self.push()
        else:
            self.push()
            self.pop()
            self.pop()
            self.pop()
        return str(self.stiva)


obiect = Stiva(1, 2, 3)
print(obiect)
# obiect_2 = Stiva("stiva2")

# obiect.push(3)
# obiect.push(2)
# obiect.push(1)
# obiect_2.push(4)
# obiect_2.push(5)
# obiect_2.push(6)
# print(obiect.stiva)
# print(obiect_2.stiva)

# print(obiect.pop())
# print(obiect.pop())
# print(obiect.pop())
# print(obiect.__dict__)
# print(Stiva.__dict__)
# print(obiect.stiva)
# print(obiect_2.stiva)
