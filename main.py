import art

print(art.cal_design)

condition = True
first_num = float(input("Enter the first number: "))

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


while condition:
    print('''Select any one operation.
 *
 +
 -
 / ''')
    operation = input("Enter your choice:- ")
    second_num = float(input("Enter the next number: "))

    for key in func_dictionary:
        if operation == key:
            value = func_dictionary[key](first_num,second_num)
            operation_symbol = key
    print(f"{first_num} {operation_symbol} {second_num} = {value}")
    cont_condition = input("Enter 'y' if you want to continue with perivious output.\
Enter 'n' if you want to start new calculation. \n")
    if cont_condition == 'y':
        first_num = value
    elif cont_condition == 'n':
        print('\n'*100)
        print(art.cal_design)
        first_num = float(input("Enter the first number: "))
