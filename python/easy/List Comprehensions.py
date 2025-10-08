if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # This is a list of all the combinations of x, y, z , make the range inclusive,the sum of the variables of the list should be different from n
    final_list = [[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if x1+y1+z1 != n]
    print(final_list)
