AppName, Version = "Calculator", "v1"
print(f"{AppName} {Version}")
operations = """
1. Addition
2. Subtraction
3. Division
4. Division
options = 1, 2, 3, and 4 
"""
while True:
    num1 = int(input("Insert the frist number > "))
    num2 = int(input("Insert the second number > "))
    print(operations)
    operation = input("Insert an operation > ")
    if operation == "1":
        RESULT = num1 + num2
        print(RESULT)
    elif operation == "2":
        RESULT = num1 - num2
        print(RESULT)
    elif operation == "3":
        RESULT = num1 * num2
        print(RESULT)
    elif operation == "4":
        try:
            RESULT = num1 / num2
            print(RESULT)
        except ZeroDivisionError:
            print("why did you break the timeli-")
    ask = input("If you want to quit type 'exit' > ")
    if ask == "exit":
        break
