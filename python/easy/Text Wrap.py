import textwrap

def wrap(string, max_width):
    # Use textwrap.fill() to wrap the input string into lines
    # each with a maximum width of max_width characters.
    # It returns the wrapped text as a single string with newline characters.
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
