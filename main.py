








def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

func_dictionary = {
    '+': add,
    '-': substract,
    '/': divide,
    '*': multiply,
}

print(func_dictionary['*'](3,4))