from termcolor import colored


def say_hello():
    print(colored("Hello, is very primitive calculate program", "cyan"))


say_hello()

a = int(input(colored("Entry number 1: ", "green")))
b = int(input(colored("Entry number 2: ", "green")))


def choice():
    i = input(colored("select '+' '*' '/' '-': ", "blue"))
    if i == "+":
        c = a + b
        print(colored("result = :", "red"), c)
    elif i == "-":
        c = a - b
        print(colored("result = :", "red"), c)
    elif i == "*":
        c = a * b
        print(colored("result = :", "red"), c)
    elif i == "/":
        c = a / b
        print(colored("result = :", "red"), c)
    else:
        print(colored("invalid entry", "yellow"))


choice()
