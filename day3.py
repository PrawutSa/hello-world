# day3.py
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are an adult")
else:
    print(f"{name}, you are a minor")