my_dict = {"jacob": [92, 98]}

print("Welcome to Student Score Manager")
print("--------------------------------")

print("1. Add new student")
print("2. Add score for existing student")
print("3. View all students and scores")
print("4. View average score for a student")
print("5. Show student with highest average")
print("6. Exit")

while True:
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        student_name = input("Enter Student Name: ").lower()
        if student_name in my_dict:
            print(f"{student_name.title()} already exists.")
        else:
            try:
                grade = float(input("Enter Score: "))
            except ValueError:
                print("Invalid score. Please enter a number.")
                continue
            my_dict[student_name] = [grade]
            print(f"{student_name.title()} added with score {grade}")

    elif option == 2:
        student_name = input("Enter Student Name: ").lower()
        if student_name in my_dict:
            try:
                grade = float(input("Enter Score: "))
            except ValueError:
                print("Invalid score. Please enter a number.")
                continue
            my_dict[student_name].append(int(grade))
            print(f"Score {grade} added for {student_name.title()}")
        else:
            print("Student not found.")

    elif option == 3:
        if not my_dict:
            print("No students in the system.")
        else:
            print("Students and Scores:")
            for student, scores in my_dict.items():
                scores_str = ", ".join(str(s) for s in scores)
                print(f"{student.title()}: {scores_str}")

    elif option == 4:
        student_name = input("Enter Student Name: ").lower()
        if student_name in my_dict:
            scores = my_dict[student_name]
            average = sum(scores) / len(scores)
            print(f"Average score for {student_name.title()}: {average}")
        else:
            print("Student not found.")

    elif option == 5:
        if not my_dict:
            print("No students in the system.")
        else:
            highest_avg = None
            top_students = []

            for student_name, scores in my_dict.items():
                average = sum(scores) / len(scores)
                if highest_avg is None or average > highest_avg:
                    highest_avg = average
                    top_students = [student_name]
                elif average == highest_avg:
                    top_students.append(student_name)

            print("Top student(s):")
            for student in top_students:
                print(f"{student.title()} with average score {highest_avg}")

    elif option == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 6.")
