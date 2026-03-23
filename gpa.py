print(" welcome to the  GPA Calculator!")
print(" this will help you calculate your gpa for the semester ")
while True:
    try:
        num_subjects = int(input(" enter the total number of subjects this semester: "))
        if num_subjects  >  0:
            break
        else:
            print(" please enter a number greater than 0 ")
    except ValueError:
        print(" invalid input. Please enter a whole number ")
total_grade_points = 0.0
total_credits_enrolled = 0
print("\n now, let's enter the details for each subject ")
for i in range(1, num_subjects + 1):
    print(f"\nSubject {i}:")
    while True:
        try:
            marks = float(input(f"Enter marks (out of 100) for Subject {i}: "))
            if 0 <= marks <= 100:
                break
            else:
                print(" Marks must be between 0 and 100 ")
        except ValueError:
            print(" Invalid input. Please enter a number for marks ")
    while True:
        try:
            credits = int(input(f" Enter credit value for Subject {i}: "))
            if credits >= 0:
                break
            else:
                print(" Credits cannot be negative ")
        except ValueError:
            print("Invalid input. Please enter a whole number for credits.")  
    grade_point = 0
    if marks >= 90:
        grade_point = 10  
        print("Grade: O (Outstanding) - Grade Point: 10")
    elif marks >= 80:
        grade_point = 9  
        print("Grade: A+ (Excellent) - Grade Point: 9")
    elif marks >= 70:
        grade_point = 8   
        print("Grade: A (Very Good) - Grade Point: 8")
    elif marks >= 60:
        grade_point = 7   
        print("Grade: B+ (Good) - Grade Point: 7")
    elif marks >= 50:
        grade_point = 6   
        print("Grade: B (Above Average) - Grade Point: 6")
    elif marks >= 45:
        grade_point = 5   
        print("Grade: C (Average) - Grade Point: 5")
    elif marks >= 40:
        grade_point = 4   
        print("Grade: P (Pass) - Grade Point: 4")
    else:
        grade_point = 0   
        print("Grade: F (Fail) - Grade Point: 0")
    subject_points = grade_point * credits
    total_grade_points += subject_points
    total_credits_enrolled += credits
print("\n" + "="*40)
print(" RESULTS")
print("="*40)
if total_credits_enrolled > 0:
    gpa = total_grade_points / total_credits_enrolled
    print(f"Total Grade Points Earned: {total_grade_points:.2f}")
    print(f"Total Credits Enrolled: {total_credits_enrolled}")
    print(f"\nYour Semester GPA is: {gpa:.2f}")
    if gpa >= 9.0:
        print(" outstanding    ")
    elif gpa >= 7.0:
        print(" very good  ")
    else:
        print(" keep pushing aiming for better next semester  ")
else:
    print(" errer ")
print("="*40)