def plus(a):
    a = input()
    b = input()
    c = a + b
    print(c)

def minus(a):
    a = input()
    b = input()
    c = a - b
    print(c)

w = input("\"+\" or \"-\"?")

if w == "+":
    plus()

elif w == "-":
    minus()

else:
    print("comand not found")
