import numpy

def arrays(arr):
    # Reverse the list using the slicing [::-1] method
    arr = arr[::-1]
    # Convert the list to a NumPy array; the second argument sets the data type to float
    arr_final = numpy.array(arr, float)
    return arr_final

arr = input().strip().split(' ')
result = arrays(arr)
print(result)