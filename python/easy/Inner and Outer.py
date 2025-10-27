import numpy

# Get the numbers x y
nums_a = [int(x) for x in input().split()]
nums_b = [int(x) for x in input().split()]

# Assign them to the numpy array [x,y]
array_a = numpy.array(nums_a)
array_b = numpy.array(nums_b)

# Compute and display results
print(numpy.inner(array_a, array_b))
print(numpy.outer(array_a, array_b))
