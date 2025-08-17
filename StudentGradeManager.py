# Student Score Manager
# This program allows you to add students, record their scores, view averages,
# and find the student(s) with the highest average score.

# Dictionary to store student names and their scores
# Keys = student names (lowercase), Values = list of scores
my_dict = {"jacob": [92, 98]}

print("Welcome to Student Score Manager")
print("--------------------------------")

# Menu options shown to the user
print("1. Add new student")
print("2. Add score for existing student")
print("3. View all students and scores")
print("4. View average score for a student")
print("5. Show student with highest average")
print("6. Exit")

# Main program loop
while True:
    try:
        # Ask user for menu choice
        option = int(input("Choose an option: "))
    except ValueError:
        # Handles case where user enters non-numeric input
        print("Please enter a valid number.")
        continue

    # Option 1: Add a new student
    if option == 1:
        student_name = input("Enter Student Name: ").lower()
        if student_name in my_dict:
            print(f"{student_name.title()} already exists.")
        else:
            try:
                grade = float(input("Enter Score: "))  # Enter first score
            except ValueError:
                print("Invalid score. Please enter a number.")
                continue
            # Store the student and their first score in the dictionary
            my_dict[student_name] = [grade]
            print(f"{student_name.title()} added with score {grade}")

    # Option 2: Add a score for an existing student
    elif option == 2:
        student_name = input("Enter Student Name: ").lower()
        if student_name in my_dict:
            try:
                grade = float(input("Enter Score: "))
            except ValueError:
                print("Invalid score. Please enter a number.")
                continue
            my_dict[student_name].append(int(grade))  # Append new score
            print(f"Score {grade} added for {student_name.title()}")
        else:
            print("Student not found.")

    # Option 3: View all students and their scores
    elif option == 3:
        if not my_dict:
            print("No students in the system.")
        else:
            print("Students and Scores:")
            for student, scores in my_dict.items():
                # Join scores into a readable string
                scores_str = ", ".join(str(s) for s in scores)
                print(f"{student.title()}: {scores_str}")

    # Option 4: View the average score for a specific student
    elif option == 4:
        student_name = input("Enter Student Name: ").lower()
        if student_name in my_dict:
            scores = my_dict[student_name]
            average = sum(scores) / len(scores)
            print(f"Average score for {student_name.title()}: {average}")
        else:
            print("Student not found.")

    # Option 5: Show student(s) with the highest average score
    elif option == 5:
        if not my_dict:
            print("No students in the system.")
        else:
            highest_avg = None
            top_students = []

            # Loop through each student and calculate average
            for student_name, scores in my_dict.items():
                average = sum(scores) / len(scores)
                # Update the highest average if found
                if highest_avg is None or average > highest_avg:
                    highest_avg = average
                    top_students = [student_name]
                elif average == highest_avg:  # Handle ties
                    top_students.append(student_name)

            # Print all students with the highest average
            print("Top student(s):")
            for student in top_students:
                print(f"{student.title()} with average score {highest_avg}")

    # Option 6: Exit the program
    elif option == 6:
        print("Goodbye!")
        break

    # Handle invalid menu input
    else:
        print("Invalid option. Please choose between 1 and 6.")
