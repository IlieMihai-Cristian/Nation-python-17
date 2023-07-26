class Rata:

    counter = 0

    def __init__(self, inaltime, greutate, sex):
        self.inaltime = inaltime
        self.greutate = greutate
        self.sex = sex
        Rata.counter += 1

    def merge(self):
        return "Merge"


obiect_1 = Rata(10, 3, 'masculin')
print(obiect_1.counter)
obiect_2 = Rata(5, 2, 'feminin')
print(obiect_2.counter)
obiect_3 = Rata(6, 4, 'masculin')
print(obiect_3.counter)
obiect_4 = Rata(6, 4, 'masculin')
print(obiect_4.counter)

