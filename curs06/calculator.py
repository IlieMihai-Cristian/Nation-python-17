class Calculator:
    def __init__(self):

        self.number1 = self.input_checker(input('Insert nr.1: '), 1)
        self.number2 = self.input_checker(input('Insert nr.2: '), 2)
        self.sign = self.sign_checker(input('Insert operation sign: '))


    def input_checker(self, param, param2):
        while param.isdigit() == False:
            param = input(f'Insert nr.{param2}: ')
        return int(param)

    def sign_checker(self, param):
        while param not in ['*', '-', '+', '/']:
            param = input('Insert operation sign: ')
        return param

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def divide(self):
        while self.number2 == 0:
            self.number2 = int(input('Insert nr.2: '))
        return self.number1 / self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def user_sign(self):
        if self.sign == '+':
            return self.addition()
        elif self.sign == '-':
            return self.subtraction()
        elif self.sign == '/':
            return self.divide()

        return self.multiplication()

    def __str__(self):
        return f'{self.number1} {self.sign} {self.number2} = {self.user_sign()}'

while True:
    x = Calculator()
    print(x)
    quit_q = input('Press Q to quit: ').lower()
    if quit_q == 'q':
        break
