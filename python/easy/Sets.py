def average(array):
    # We need the distinct heights so we remove the duplicates by casting the array to a set
    array_to_set = set(array)
    # Caclculate the total sum of the set
    total = sum(array_to_set)
    # Compute the average
    average = total/ len(array_to_set)
    return average 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
