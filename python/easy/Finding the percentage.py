if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # Loop through the key/ avlue pairs of the dictionary
    for key, value in student_marks.items():
        if key == query_name: # if the name matches find the average score
            average = 0
            total = 0        
            for val in value:
                total += val
            average = total/len(value)
            print(f"{average:.2f}") # use :.2f to print with two decimals
