try:
    x = int(input("Enter a number: "))
    result = 12/x
except ZeroDivisionError:
    print("Please enter something else")