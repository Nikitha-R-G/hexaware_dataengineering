# Python Capstone Project
#
# Student Performance and Activity Analyzer
#
# Objective
#
# Build a Python program that reads data from:
# students.txt
# marks.json
# attendance.csv
# Then analyze the data and generate a final summary report.
#
# Project Files
#
# 1. students.txt
#
# Rahul
# Sneha
# Arjun
# Priya
# Karan
# Rahul
# Sneha
#
# 2. marks.json
#
# {
# "students": [
# {"name": "Rahul", "marks": 85, "course": "Python"},
# {"name": "Sneha", "marks": 92, "course": "Data Engineering"},
#
# {"name": "Arjun", "marks": 78, "course": "Python"},
# {"name": "Priya", "marks": 88, "course": "AI"},
# {"name": "Karan", "marks": 70, "course": "Python"}
# ]
# }
#
# 3. attendance.csv
#
# name,days_present,total_days
# Rahul,22,25
# Sneha,24,25
# Arjun,20,25
# Priya,23,25
# Karan,18,25
#
# Part 1 — Basics and File Handling
#
# Task 1
#
# Read students.txt and print all names.
students=[]
with open("students.txt","r") as file:
    for line in file:
        students.append(line.strip())
print("students from student.txt:",students)
# Task 2
#
# Count the total number of entries in students.txt .
count_entries_students=len(students)
print("Count the total number of entries in students.txt :",count_entries_students)
#
# Task 3
#
# Find the unique student names using a set.
unique_students=set(students)
print("the unique student names using a set:",unique_students)
# Task 4
#
# Count how many times each student name appears using a dictionary.
student_appear={}
for s in students:
    if s in student_appear:
        student_appear[s]+=1
    else:
        student_appear[s]=1
print("times each student name appears using a dictionary:",student_appear)
# Task 5
#
# Write the unique student names into a new file called unique_students.txt .
with open("unique_students.txt","w") as file:
    for u in unique_students:
        file.write(u)
        file.write("\n")
print("the unique student names into a new file called unique_students.txt written successfully!!!")

#
# Part 2 — JSON Handling
#
# Task 6
#
# Read marks.json .
import json
with open("marks.json","r") as file:
   marks= json.load(file)

#
# Task 7
#
# Print all student names and marks.
print(" All student names and marks:")
for m in marks["students"]:
    print(m["name"],m["marks"])
#
# Task 8
#
# Find the student with the highest marks.
highest_mark=0
for m in marks["students"]:
    if m["marks"]>highest_mark:
        highest_mark=m["marks"]
        s=m["name"]
print("the student with the highest marks:",s,"mark:",highest_mark)
# Task 9
#
# Find the student with the lowest marks.
lowest_mark=100
for m in marks["students"]:
    if m["marks"]<lowest_mark:
        lowest_mark=m["marks"]
        s=m["name"]
print("the student with the lowest marks:",s,"mark:",lowest_mark)
#
# Task 10
#
# Calculate the average marks.
average_mark=0
total=0
count=0
for m in marks["students"]:
    total+=m["marks"]
    count+=1
average_mark=total/count
print("the student with the average marks:",average_mark)
# Task 11
#
# Print only students enrolled in the Python course.
print("Only students enrolled in the Python course:")
for m in marks["students"]:
    if m["course"]=="Python":
        print(m["name"])

# Task 12
#
# Count how many students are there in each course using a dictionary.
student_count_course={}
for m in marks["students"]:
    if m["course"] in student_count_course:
        student_count_course[m["course"]]+=1
    else:
        student_count_course[m["course"]]=1
print("students are there in each course using a dictionary:",student_count_course)
#
# Part 3 — CSV Handling
#
# Task 13
#
# Read attendance.csv .
import csv
attendance={}
with open("attendance.csv","r") as file:
    lines = file.readlines()[1:]
for line in lines:
    name, days_present, total_days=line.strip().split(",")
    attendance[name]={
        "days_present":int(days_present),
        "total_days":int(total_days)
    }
#
# Task 14
#
# Print each student’s attendance details.
print( "each student’s attendance details:",attendance)

#
# Task 15
#
# Calculate attendance percentage for each student.
# Formula:
#
# (days_present / total_days) * 100
print("attendance percentage for each student:")
attendance_percentage={}
for name,details in attendance.items():
    present=details["days_present"]
    total=25
    percentage=(present/total)*100
    attendance_percentage[name]=percentage
    print(name,":",percentage)
print(attendance_percentage)

#
# Task 16
#
# Print students whose attendance is below 80%.
print("students whose attendance is below 80%:")
for k in attendance_percentage:
    if attendance_percentage[k]<80:
        print(k,":",attendance_percentage[k])
#
# Task 17
#
# Find the student with the best attendance.
print(" the student with the best attendance:")
max_attendance=0
for k in attendance_percentage:
    if attendance_percentage[k]>max_attendance:
        max_attendance=attendance_percentage[k]
        name=k
print(name,":",max_attendance)
#
# Part 4 — Data Structures Practice
#
# Task 18
#
# Store all marks in a list and print:
list_mark=[]
print("all marks in a list:")
for m in marks["students"]:
    list_mark.append(m["marks"])
print(list_mark)
# highest marks
print("highest marks:",max(list_mark))
# lowest marks
print("lowest marks:",min(list_mark))
# sum of marks
print("sum of  marks:",sum(list_mark))
#
# Task 19
#
# Create a tuple of all courses and print it.
tuple_courses=[]
print("a tuple of all courses:")
for m in marks["students"]:
    tuple_courses.append(m["course"])
print(tuple(tuple_courses))
# Task 20
#
# Create a set of all courses to show unique courses.
print("A set of all courses to show unique courses :",set(tuple_courses))
#
# Task 21
#
# Create a dictionary where:
# key = student name
# value = marks
student_dict={}
for m in marks["students"]:
    name=m["name"]
    marks=m["marks"]
    student_dict[name]=marks
print("dict-1:key = student name,value = marks")
print(student_dict)
#
# Task 22
#
# Create a second dictionary where:
# key = student name
# value = attendance percentage
print("dict2:key = student name value = attendance percentage")
print(attendance_percentage)
#
# Part 5 — Conditions and Loops
#
# Task 23
#
# Using a loop, print whether each student is:
# "Pass" if marks >= 50
# "Fail" otherwise
print("whether each student is pass or fail:")
for s in student_dict:
    if student_dict[s]>=50:
        print(s,":","pass")
    else:
        print(s, ":", "fail")
#
# Task 24
#
# Using conditions, assign grades:
# 90 and above → A
# 75 to 89 → B
# 50 to 74 → C
# below 50 → Fail
print("grade of each student:")
for s in student_dict:
    if student_dict[s]>=90:
        print(s,":","A")
    elif 89>=student_dict[s]>=75:
        print(s,":","B")
    elif 74 >= student_dict[s] >= 50:
        print(s,":","C")
    else:
        print(s, ":", "fail")
#
# Task 25
#
# Print all students who have:
# marks above 80
# attendance above 85%
print("Print all students who have: marks above 80 attendance above 85%:")
for s in student_dict:
    if student_dict[s]>80 and attendance_percentage[s]>85:
        print(s)
#
# Part 6 — Functions
#
# Create separate functions for the following:
# Task 26
#
# A function to read names from students.txt .
def load_students(filename):
    students = []
    with open(filename, "r") as file:
        for line in file:
            students.append(line.strip())
    return students
#
# Task 27
#
# A function to load student marks from marks.json .
import json

def load_marks(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["students"]
#
# Task 28
#
# A function to load attendance from attendance.csv .
def load_attendance(filename):
    attendance = {}

    with open(filename, "r") as file:
        lines = file.readlines()[1:]

    for line in lines:
        name, present, total = line.strip().split(",")

        attendance[name] = {
            "days_present": int(present),
            "total_days": int(total)
        }

    return attendance
#
# Task 29
#
# A function to calculate average marks.
def average_marks(students):
    total = sum(s["marks"] for s in students)
    return total / len(students)
# Task 30
#
# A function to calculate attendance percentage.
def attendance_percentage(attendance):
    percentage = {}

    for name, details in attendance.items():
        present = details["days_present"]
        total = details["total_days"]
        percentage[name] = (present / total) * 100

    return percentage
# Task 31
#
# A function to return the topper.
def find_topper(students):
    topper = max(students, key=lambda x: x["marks"])
    return topper["name"]
# Task 32
#
# A function to generate grade for a mark.
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"
#
# Part 7 — Final Combined Analysis
#
# Task 33
#
# Combine marks and attendance data and create a final structure like this:
def combine_data(students, attendance_per):
    final = {}

    for s in students:
        name = s["name"]

        final[name] = {
            "marks": s["marks"],
            "course": s["course"],
            "attendance": attendance_per[name],
            "grade": grade(s["marks"])
        }

    return final
#
# Task 34
#
# From this combined structure, print:
# name
# marks
# attendance
# course
# grade
def print_report(data):
    for name, info in data.items():
        print(
            name,
            "- Marks:", info["marks"],
            "- Attendance:", info["attendance"],
            "- Course:", info["course"],
            "- Grade:", info["grade"]
        )
# Task 35
#
# Find students who are eligible for certification.
# Condition:
# marks >= 75
# attendance >= 80
def eligible_students(data):
    eligible = []

    for name, info in data.items():
        if info["marks"] >= 75 and info["attendance"] >= 80:
            eligible.append(name)

    return eligible
#
# Task 36
#
# Find students who need improvement.
# Condition:
# marks < 75 or attendance < 80
def need_improvement(data):
    improve = []

    for name, info in data.items():
        if info["marks"] < 75 or info["attendance"] < 80:
            improve.append(name)

    return improve
#
# Part 8 — Output File Generation
#
# Task 37
#
# Write the final student summary to a text file called report.txt .
# {
# "Rahul": {"marks": 85, "attendance": 88.0, "course": "Python"},
# "Sneha": {"marks": 92, "attendance": 96.0, "course": "Data Engineerin
# }
def write_report(data):
    with open("report.txt", "w") as f:
        f.write("Student Report\n")

        for name, info in data.items():
            line = (
                f"{name} - Marks: {info['marks']} "
                f"- Attendance: {info['attendance']}% "
                f"- Grade: {info['grade']}\n"
            )
            f.write(line)
#
# Expected style:
#
# Student Report
# Rahul - Marks: 85 - Attendance: 88.0% - Grade: B
# Sneha - Marks: 92 - Attendance: 96.0% - Grade: A
# Arjun - Marks: 78 - Attendance: 80.0% - Grade: B
#
# Task 38
#
# Write only eligible students to eligible_students.txt .
def write_eligible(names):
    with open("eligible_students.txt", "w") as f:
        for name in names:
            f.write(name + "\n")
#
# Final Challenge
#
# Task 39
#
# Generate this final console output:
#
# Topper: Sneha
# Best Attendance: Sneha
# Average Marks: 82.6
# Eligible Students: Rahul, Sneha, Priya
# Students Needing Improvement: Karan

#
# Task 40
#
# Make the program modular using functions and keep the code clean.
def main():

    students_list = load_students("students.txt")
    marks_data = load_marks("marks.json")
    attendance_data = load_attendance("attendance.csv")

    attendance_per = attendance_percentage(attendance_data)

    final_data = combine_data(marks_data, attendance_per)

    avg = average_marks(marks_data)
    topper = find_topper(marks_data)

    best_attendance = max(attendance_per, key=attendance_per.get)

    eligible = eligible_students(final_data)
    improve = need_improvement(final_data)

    print("\nFinal Output")
    print("Topper:", topper)
    print("Best Attendance:", best_attendance)
    print("Average Marks:", round(avg, 1))
    print("Eligible Students:", ", ".join(eligible))
    print("Students Needing Improvement:", ", ".join(improve))

    write_report(final_data)
    write_eligible(eligible)


main()