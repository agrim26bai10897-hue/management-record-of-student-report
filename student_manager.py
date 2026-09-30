from data_store import students
from academic_engine import calculate_academic_performance, prompt_marks_input

def display_record(student_id):
    """Displays single student record."""
    if student_id not in students:
        print("\nStudent NOT FOUND!")
        return
        
    student = students[student_id]
    print("\n==================================")
    print("        STUDENT RECORD")
    print("==================================")
    print("Student ID :", student_id)
    print("Name       :", student["Name"])
    print("Age        :", student["Age"])
    print("Status     :", student["Status"])
    print("State      :", student["State"])
    print("Course     :", student["Course"])
    print("Semester   :", student["Semester"])
    print("----------------------------------")
    
    marks = student.get("Marks", {})
    if marks:
        print("Marks      :", marks)
        print("Total      :", student.get("Total", 0))
        print("Percentage :", student.get("Percentage", 0.0), "%")
        print("Result     :", student.get("Result", "N/A"))
    print("==================================")

def search_student():
    """Searches and displays student record."""
    student_id = input("\nEnter Student ID: ").upper()
    display_record(student_id)

def add_student():
    """Adds a new student to dictionary."""
    print("\n===========================")
    print("        ADD NEW STUDENT")
    print("===========================")

    student_id = input("Enter Student ID: ").upper()
    if student_id in students:
        print("\nStudent ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    status = input("Enter Status (Hosteller/Day Scholar): ")
    state = input("Enter State: ").upper()
    course = input("Enter Course: ").upper()
    semester = int(input("Enter Semester: "))

    # Get academic marks
    marks = prompt_marks_input()
    total, percentage, result = calculate_academic_performance(marks)

    students[student_id] = {
        "Name": name,
        "Age": age,
        "Status": status,
        "State": state,
        "Course": course,
        "Semester": semester,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Result": result
    }
    
    print("\nStudent Added Successfully!")

def update_marks():
    """Updates marks for an existing student."""
    student_id = input("\nEnter Student ID to update marks: ").upper()
    if student_id not in students:
        print("\nStudent NOT FOUND!")
        return

    print("\nUpdating marks for", students[student_id]["Name"])
    marks = prompt_marks_input()
    total, percentage, result = calculate_academic_performance(marks)

    students[student_id]["Marks"] = marks
    students[student_id]["Total"] = total
    students[student_id]["Percentage"] = percentage
    students[student_id]["Result"] = result

    print("\nMarks and Results Updated Successfully!")

def display_all_students():
    """Displays list of all students."""
    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n==========================================================================")
    print("                           ALL STUDENT RECORDS                            ")
    print("==========================================================================")
    for s_id in students:
        s = students[s_id]
        print("ID:", s_id, "| Name:", s["Name"], "| Course:", s["Course"], "| %:", s.get("Percentage", 0.0), "| Result:", s.get("Result", "N/A"))
    print("==========================================================================")