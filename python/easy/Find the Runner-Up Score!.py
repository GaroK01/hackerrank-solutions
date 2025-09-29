if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # cast the list to a set, so we remove the duplicates
    # use reverse = True, to sort in descending order
    final_arr = sorted(set(arr), reverse = True)
    # print the second highest element
    print(final_arr[1])
