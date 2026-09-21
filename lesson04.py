age = int(input("Enter your age:  "))

if age >= 18:
    print("Access granted.")
elif age >= 13:
    print("Access granted with parental permission.")
else:
    print("Access denied.")