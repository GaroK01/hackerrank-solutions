if __name__ == '__main__':
    N = int(input())
    command_count = 0
    my_list = []

    while command_count < N:
        # Read the input line, strip whitespace, and split into parts
        parts = input().strip().split()
        # The first part is the command
        cmd = parts[0]
        # The rest are arguments (converted from strings to integers)
        args = list(map(int, parts[1:]))

        if cmd == "insert":
            my_list.insert(args[0], args[1])
        elif cmd == "append":
            my_list.append(args[0])
        elif cmd == "remove":
            my_list.remove(args[0])
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()
        elif cmd == "print":
            print(my_list)
            
        command_count += 1    
