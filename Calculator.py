print("\t\t***Easy Calculator!***\t\t")

def do_operation(operand, num1, num2):
 if operand  == '*' or operand  == 'x' or operand == 'X':
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
    check_operands = ['+','-','*', '/', 'x', 'X', '^', '%']
    partitions = []
    op = ''

    #check for one of the valid operators from the 'operands' list
    for chr in check_operands:
        if input_str.find(chr) > -1: #the find() function returns the index where a sub-string is found. it returns '-1' otherwise
            op = chr # set op to the operator character/sysmbol that was found
        
    partitions = input_str.partition(op)# 'partition()' returns a 3-tuple. the first partition [0], the seperator[1], and the last partition[2]
    numA = float(partitions[0])
    numB = float(partitions[2])
    operator = partitions[1]
    return (numA, numB, operator) #return a tuple with two floats and one str/char
    
quit = False

while(not quit):
    try:
        (num1, num2, operand) = split_str(str(input(">")))

        print("Answer: " + str(do_operation(operand, num1, num2)))

        if operand == "%":
            print("*NB: modulous function may return inaccurate results when using doubles and floats")

        print()

        num1 = num2 = 0.0

    except ZeroDivisionError:
         print("Can't divide by zero!")

    except ValueError:
         print("Invalid Input!")

    except:
        print("Error! no spaces allowed ")
    




