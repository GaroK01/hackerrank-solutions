if __name__ == '__main__':
    # Initialize the variables needed
    n = int(input())
    students = []
    grades = []
    names = []
    
    # Adding the students with their grades    
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Save the grades in the list
    for student in students:
        grades.append(student[1])

    # First we remove the duplicated grades, then we sort them
    unique_grades = sorted(set(grades))
    # We get the second lowest grade
    second_lowest = unique_grades[1]
    
    # We find students with the second lowest garde and add them in the list
    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    # Then we sort alphabetically and print the names
    for name in sorted(names):
        print(name)
