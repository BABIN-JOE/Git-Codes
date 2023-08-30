while True:
    num1 = float(input("Enter the number 1 : "))
    num2 = float(input("Enter the number 2 : "))
    operator = input("Enter the operator ('+' \ '-' \ '*' \ '/') : ")

    if(operator == '+'):
        print(num1 + num2)
    elif(operator == '-'):
        print(num1 - num2)
    elif(operator == '*'):
        print(num1 * num2)
    elif(operator == '/'):
        print(num1 / num2)
    else:
        print("Invalid Operator")

    Next_Calculation = input("Do you want another calculation ? (y/n) : ")
    if Next_Calculation == "y":
        continue
    elif Next_Calculation == "n":
        break
    break 
