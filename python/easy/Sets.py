def average(array):
    # Calculate the total sum of the array
    total = sum(array)
    # Compute the average
    average = total / len(array)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  
    result = average(arr)
    print(result)