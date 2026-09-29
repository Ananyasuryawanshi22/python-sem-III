import csv
import json

# Store student details in CSV file
students = [
    [1, "Ananya", "CSE", 85, 90, 80],
    [2, "Rahul", "IT", 75, 80, 70],
    [3, "Priya", "AIML", 95, 92, 88]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["RollNo", "Name", "Branch", "Marks1", "Marks2", "Marks3"])

    for student in students:
        writer.writerow(student)


# Read CSV file and process records
processed_students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        marks1 = int(student["Marks1"])
        marks2 = int(student["Marks2"])
        marks3 = int(student["Marks3"])

        total = marks1 + marks2 + marks3
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        processed_students.append({
            "RollNo": int(student["RollNo"]),
            "Name": student["Name"],
            "Branch": student["Branch"],
            "Total": total,
            "Percentage": percentage,
            "Grade": grade
        })


# Store processed records in JSON file
with open("students.json", "w") as file:
    json.dump(processed_students, file, indent=4)

print("Student records processed successfully!")