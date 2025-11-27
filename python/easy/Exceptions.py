T = int(input())
for _ in range(T):
    inputs = input().split()
    try:
        a = int(inputs[0])
        b = int(inputs[1])
        result = a // b
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as err:
        print("Error Code:", err)
    else:
        print(result)
