if __name__ == '__main__':
    s = input()
    # Check if the string contains at least one of each: alphanumeric, alphabetic, digit, lowercase, and uppercase character
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
