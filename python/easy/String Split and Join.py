def split_and_join(line):
    # Split the string into a list using the delimiter (" ")
    # Then join the words using the separator ("-")
    return "-".join(line.split(" "))
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
