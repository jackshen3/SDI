def sorting_app():
    print("Welcome to the Grade Sorter App")
    grades = [] # Initialize a list
    first_grade = input("What is your first grade (0-100): ")
    second_grade = input("What is your second grade (0-100): ")
    third_grade = input("What is your third grade (0-100): ")
    fourth_grade = input("What is your fourth grade (0-100): ")
    for i in (first_grade, second_grade, third_grade, fourth_grade):
        grades.append(int(i)) # Adds new values to the list "grades"
    print("Your grades are:", grades)
    grades.sort(reverse=True)
    print("Your grades from highest to lowest are:", grades)
    print("The lowest two grades will now be dropped.")
    for i in range(2):
        print("Removed grade:", min(grades))
        grades.remove(min(grades))
    print("Your remaining grades are:", grades)
    if max(grades) >= 80:
        print("Nice work! Your highest grade is a", max(grades) + "")
    elif max(grades) <= 84:
        print("Wow go study. Your highest grade is a", max(grades) + "")
    
sorting_app()