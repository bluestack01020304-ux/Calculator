import Utility.Calculator

a = ''

b = ''

while(True):
    b = input()

    if b== "계산":
        b = Utility.Calculator.calcul(a)

    a = a+b
    print(a)