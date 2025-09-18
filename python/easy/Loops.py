if __name__ == '__main__':
    n = int(input())
    i = 0  # Initialize the counter starting at 0
    
    # Check if the number given is in the range
    if 1 <= n <= 20:
        while i < n: # While the counter is less than n
            print(i * i) # Print the square of the counter
            i += 1 # Increment by 1
