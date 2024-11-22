#w4q5
students = []

def newStudent(name, roll, year, course):
    # Create a dictionary for the new student
    student = {"Name": name, "Roll": roll, "Year": year, "Course": course}
    # Append the dictionary to the students list
    students.append(student)
    
def display(roll):
    # Iterate through the students list to find the student with the matching roll number
    for student in students:
        if student["Roll"] == roll:
            print("Name:", student["Name"])
            print("Roll Number:", student["Roll"])
            print("Year:", student["Year"])
            print("Course:", student["Course"])
            return  # Stop after finding the first match

# Adding students
newStudent("Talha", 112, 2022, "Cybersecurity")
newStudent("Rayyan", 109, 2022, "Cybersecurity")
newStudent("Ahwar", 124, 2020, "MBA")

# Displaying a student with roll number 112
display(112)
