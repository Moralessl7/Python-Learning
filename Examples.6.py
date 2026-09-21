print("=== WELCOME TO THE MULTIPLICATION TABLE OF NUMBERS ===")
number = int(input("Enter the number you want to see the multiplication table of:  "))
for i in range (1, 11):
    result = number * i
    print(number, "x", i, "=", result)