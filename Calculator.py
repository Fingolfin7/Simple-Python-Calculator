print("\t\t***Easy Calculator!***\t\t")


def do_operation(operand, num1, num2):
    if operand == '*' or operand == 'x' or operand == 'X':
        return num1 * num2
    elif operand == '/':
        return num1 / num2
    elif operand == '-':
        return num1 - num2
    elif operand == '+':
        return num1 + num2
    elif operand == '^':
        return pow(num1, num2)
    elif operand == '%':
        return num1 % num2
    else:
        return 0


def split_str(input_str):
    operands = ['+', '-', '*', '/', 'x', 'X', '^', '%']
    length = len(input_str)

    def findOperatorIndex(query_str):
        for index in range(1, length):
            str_chr = query_str[index]
            for val in operands:
                if val == str_chr:
                    return index
        return -1

    operatorIndex = findOperatorIndex(input_str)

    numA = float(str(input_str[0: operatorIndex]))
    numB = float(str(input_str[operatorIndex + 1: length]))

    return numA, numB, input_str[operatorIndex]  # return a tuple with two floats and one str/char


Quit = False

while not Quit:
    try:
        userInput = str(input("> "))
        if userInput.lower() == "quit" or userInput.lower() == "exit" or userInput.lower() == "q":
            Quit = True
        else:
            (num1, num2, operand) = split_str(userInput)

            print("Answer: " + str(do_operation(operand, num1, num2)))

            if operand == "%":
                print("*NB: modulus function may return inaccurate results when using doubles and floats")

            print()

            num1 = num2 = 0.0

    except ZeroDivisionError:
        print("Can't divide by zero!")

    except ValueError:
        print("Invalid Input!")
