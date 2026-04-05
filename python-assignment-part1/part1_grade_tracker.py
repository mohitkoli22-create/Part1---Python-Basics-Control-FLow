# TASK1 - Data parsing and cleaning

# Raw student data


raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Initialize list to store cleaned students
cleaned_students = []

# Process each student
for student in raw_students:
    # Step 1: Clean name
    name = student["name"].strip().title()

    # step 2: Convert roll to int
    roll = int(student["roll"])

    # Step 3: Convert marks_str to list of ints
    marks = list(map(int, student["marks_str"].split(",")))

    # validate name
    is_valid = all(word.isalpha() for word in name.split())

    print("✓ Valid name" if is_valid else "✗ Invalid name")

    # PRINT PROFILE CARD
    print("=" * 32)
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print(f"Marks: {marks}")
    print("=" * 32)

    cleaned_students.append({"name":name, "roll":roll, "marks":marks})



# print profile card for student with roll 101
for student in cleaned_students:
    if student["roll"] == 101:
        print("=" * 32)
        print(f"Name: {student['name']}")
        print(f"Roll: {student['roll']}")
        print(f"Marks: {student['marks']}")
        print("=" * 32)
        break


# Task2 - Marks Analysis Using Loops & Conditionals

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# Grade labelling based on marks
def get_grade(mark):
    if 90 <= mark <= 100:
        return "A+"
    elif 80 <= mark <= 89:
        return "A"
    elif 70 <= mark <= 79:
        return "B"
    elif 60 <= mark <= 69:
        return "C"
    else:
        return "F"

# Print subjects + grades
for subject, mark in zip(subjects, marks):
    grade = get_grade(mark)
    print(f"{subject}: {mark} - Grade: {grade}")

# Calculations     

# total marks
total_marks = sum(marks)

# average marks
average_marks = total_marks / len(marks)

# highest scoring subject
highest_mark = max(marks)
highest_subject = subjects[marks.index(highest_mark)]

# lowest scoring subject
lowest_mark = min(marks)
lowest_subject = subjects[marks.index(lowest_mark)]    

print(total_marks)
print(average_marks)
print(highest_mark, highest_subject)
print(lowest_mark, lowest_subject)


new_count = 0   # counts new subjects added

while True:
    subject = input("\nEnter subject name (or type 'done' to stop): ")

    # STOP condition
    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0–100): ")

    # Check if input is numeric
    if not mark_input.isdigit():
        print("⚠️ Invalid input! Please enter a number.")
        continue

    mark = int(mark_input)

    # Check valid range
    if mark < 0 or mark > 100:
        print("⚠️ Marks must be between 0 and 100.")
        continue

    # Add valid data
    subjects.append(subject)
    marks.append(mark)
    new_count += 1

    print("✅ Subject added successfully!")

# After loop ends
print("\n📊 Summary:")
print("New subjects added:", new_count)

average = round(sum(marks) / len(marks), 2)
print("Updated average:", average)


# Task 3 — Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Initialize counters
pass_count = 0
fail_count = 0
topper_avg = 0
topper_name = ""
averages = []

# Calculate average for each student and result status

for name, student_marks in class_data:
    avg = sum(student_marks) / len(student_marks)

    if avg >= 60:
        result = "Pass"
    else:
        result = "Fail"

    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    averages.append(avg)
    print(f"{name:<18} | {avg:^7.2f} | {result}")

# class average
class_avg = round(sum(averages) / len(averages), 2)

print("\nPassed:", pass_count)
print("Failed:", fail_count)
print("Topper:", topper_name, topper_avg)
print("Class Average:", class_avg)


# Task 4 — String manipulation utility

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# remove leading/trailing spaces
clean_essay = essay.strip() 
print(1., clean_essay)

# Title case
print(2., clean_essay.title())

# Count occurrences of "python"
print(3., clean_essay.count("python"))

# Replace "python" with "Python"
print(4., clean_essay.replace("python", "Python"))

#split into sentences
sentences = clean_essay.split(". ")
print(5., sentences)

#print each sentence on new line
print(6.)
for i, s in enumerate(sentences, 1):
    print(f"Sentence {i}: {s.strip()}")