import art

condition = True

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

def calculator():
    print(art.cal_design)
    first_num = float(input("Enter the first number: "))
    while condition:
        print('Select your operation')
        for key in func_dictionary:
            print(key)
        operation = input("Enter your choice: ")
        second_num = float(input("Enter the next number: "))
        value = func_dictionary[operation](first_num,second_num)
        print(f"{first_num} {operation} {second_num} = {value}")
        cont_condition = input("Enter 'y' if you want to continue with perivious output. Enter 'n' if you want to start new calculation. \n")
        if cont_condition == 'y':
            first_num = value
        elif cont_condition == 'n':
            print('\n'*100)
            calculator()

calculator()