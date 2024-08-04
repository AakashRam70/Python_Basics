num1 = int(input("Enter the value 1:-"))
num2 = int(input("Enter the value 2:-"))
print(
    '''
    + Addition
    - Substraction
    * Multipication
    / Division
    '''
)
operator = input("Enter any one of this operator{+,-,*,/} :")

if operator == "+":
    print(num1+num2)

elif operator == "-":
    print(num1-num2)

elif operator == "*":
    print(num1*num2)

elif operator == "/":
    print(num1/num2)

else:
    print("Invalid Operation...")