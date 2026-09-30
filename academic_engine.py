def calculate_academic_performance(marks_dict):
    """Calculates total marks, percentage, and pass/fail result."""
    if not marks_dict:
        return 0, 0.0, "N/A"
    
    total = 0
    for subject in marks_dict:
        total = total + marks_dict[subject]
        
    percentage = round(total / len(marks_dict), 2)
    
    # Passing criteria: At least 40 marks in every subject and overall 40%
    passed_all = True
    for subject in marks_dict:
        if marks_dict[subject] < 40:
            passed_all = False
            
    if passed_all and percentage >= 40.0:
        result = "Pass"
    else:
        result = "Fail"
        
    return total, percentage, result

def prompt_marks_input():
    """Takes input for subject marks."""
    subjects = ["Math", "Physics", "CS"]
    marks = {}
    
    print("\n--- ENTER MARKS (Out of 100) ---")
    for sub in subjects:
        score = float(input("Enter marks for " + sub + ": "))
        marks[sub] = score
                
    return marks