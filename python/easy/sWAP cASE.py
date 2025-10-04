def swap_case(s):
    # swapcase() returns a copy of the input string with uppercase characters converted to lowercase and lowercase characters converted to uppercase.
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
