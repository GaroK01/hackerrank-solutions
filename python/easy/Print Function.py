if __name__ == '__main__':
    n = int(input())
    i = 1 # Initialize to 1 to not print the 0 at the beginning
    
    if 1 <= n <= 150: # Add the constraint for the number
        while i <= n:
            print(i, end = "") # end = "" is used to avoid going to a new line after print
            i += 1
            
