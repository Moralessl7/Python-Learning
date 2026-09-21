
print("=== THE HIGHEST NUMBER GAME ===")

number1 = float(input("Enter the first number:  "))
number2 = float(input("Enter the second number:  "))
number3 = float(input("Enter the third number:  "))

if number1 > number2 and number1 > number3:
    print("The highest number is:", number1)
if number2 > number1 and number2 > number3:
    print("The highest number is:", number2)
if number3 > number1 and number3 > number2:
    print("The highest number is:", number3)
elif number1 == number2 == number3:
    print("It´s a tie!")