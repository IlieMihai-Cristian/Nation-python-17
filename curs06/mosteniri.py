class A:
    pass
    # def info(self):
    #     print('Class A')

class F:
    def info(self):
        print('class F')
class B(A, F):

    pass
    # def info(self):
    #     print('Class B')
class E:
    def info(self):
        print('Class e')


class C(E):
    pass
    # def info(self):
    #     print("Class C")
class D(E, C):
    pass
    # def info(self):
    #     print("Class D")

D().info()
