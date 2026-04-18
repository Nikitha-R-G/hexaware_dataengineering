# Exercise 1 — TXT File (Login Logs)
#
# File: logins.txt
#
# Rahul
# Sneha
# Rahul
# Arjun
# Sneha
# Rahul
# Karan
#
# Questions
#
# 1. Read the file and print all names.
count=0
with open("logins.txt","r") as file:
    for line in file:
        print(line.strip())
        count +=1

# 2. Count the total number of login records.
print("total number of login records:",count)

# 3. Find how many times each user logged in.
d={}
with open("logins.txt","r") as file:
    for line in file:
        name = line.strip()
        if name in d:
            d[name]+=1
        else:
            d[name]=1
print(d)
# 4. Find the user who logged in the most.
print(max(d,key=d.get))
# 5. Print the unique users.
print(set(d))
# Exercise 2 — TXT File (Numbers Dataset)
#
# File: numbers.txt
#
# 45
# 67
# 23
# 89
# 12
# 90
# 56
# 34
# 78
# 21
#
# Questions
#
# 1. Read all numbers from the file.
a=[]
with open("numbers.txt","r") as file:
    for line in file:
        a.append(int(line.strip()))
        print(line.strip())
print(a)
# 2. Calculate the sum of all numbers.
sum=0
with open("numbers.txt","r") as file:
    for line in file:
        sum+=int(line.strip())
print(sum)
# 3. Find the maximum number.
print("max:",max(a))
# 4. Find the minimum number.
print("min:",min(a))
# 5. Count how many numbers are greater than 50.
count=0
for i in a:
    if i>50:
        count+=1
print(count)
# Exercise 3 — JSON File (Student Dataset)
#
# File: students.json
#
# {
# "students": [
# {"name": "Rahul", "marks": 85, "course": "Python"},
# {"name": "Sneha", "marks": 92, "course": "Data Science"},
# {"name": "Arjun", "marks": 78, "course": "Python"},
# {"name": "Priya", "marks": 88, "course": "AI"},
# {"name": "Karan", "marks": 70, "course": "Python"}
# ]
# }
#
# Questions
#
# 1. Print all student names.
import json
with open("students.json","r") as file:
    data=json.load(file)
for s in data["students"]:
    print(s["name"])

# 2. Print students enrolled in Python course.
for s in data["students"]:
    if s["course"]=="Python":
        print(s["name"])
# 3. Find the student with highest marks.
highest = data["students"][0]

for student in data["students"]:
    if student["marks"] > highest["marks"]:
        highest = student

print(highest["name"])
# 4. Calculate average marks.
total=0
count=0
for student in data["students"]:
    total+=student["marks"]
    count+=1
avg=total/count
print(avg)
# 5. Count how many students are enrolled in each course.
d={}
for s in data["students"]:
    course = s["course"]
    if course in d:
        d[s["course"]]+=1
    else:
        d[s["course"]] = 1
print(d)
# Exercise 4 — JSON File (E-commerce Orders)
#
# File: orders.json
#
# {
# "orders": [
# {"order_id": 1, "customer": "Rahul", "amount": 2500},
# {"order_id": 2, "customer": "Sneha", "amount": 1800},
# {"order_id": 3, "customer": "Rahul", "amount": 3200},
# {"order_id": 4, "customer": "Arjun", "amount": 1500},
# {"order_id": 5, "customer": "Sneha", "amount": 2100}
# ]
# }
#
# Questions
#
# 1. Print all orders.
with open("orders.json","r") as file:
    data=json.load(file)
for s in data["orders"]:
    print(s)
# 2. Calculate total revenue.
total=0
for order in data["orders"]:
    total+=order["amount"]
print(total)
# 3. Find total spending per customer.
d = {}

for s in data["orders"]:
    customer = s["customer"]
    amount = s["amount"]

    if customer in d:
        d[customer] += amount
    else:
        d[customer] = amount

print(d)
# 4. Find the highest spending customer.
print(max(d,key=d.get))
# 5. Count total orders per customer.
di={}
for s in data["orders"]:
    customer = s["customer"]
    if customer in di:
        di[s["customer"]]+=1
    else:
        di[s["customer"]] = 1
print(di)
# Exercise 5 — CSV File (Employee Dataset)
#
# File: employee.csv
#
# name,department,salary
# Rahul,IT,70000
# Sneha,HR,60000
# Arjun,IT,75000
# Priya,Finance,80000
# Karan,IT,72000
#
# Questions
with open("employee.csv", "r") as file:
    lines = file.readlines()[1:]
# 1. Print all employee names.
for line in lines:
    name, dept, salary = line.strip().split(",")
    print(name)
# 2. Find employees working in IT department.
for line in lines:
    name, dept, salary = line.strip().split(",")
    if dept == "IT":
        print(name)
# 3. Calculate the average salary.
total_salary = 0
count = 0

for line in lines:
    name, dept, salary = line.strip().split(",")
    total_salary += int(salary)
    count += 1

avg_salary = total_salary / count
print(avg_salary)
# 4. Find the highest salary employee.
highest_name = ""
highest_salary = 0

for line in lines:
    name, dept, salary = line.strip().split(",")
    salary = int(salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

print(highest_name, highest_salary)
# 5. Count how many employees belong to each department.
dept_count = {}

for line in lines:
    name, dept, salary = line.strip().split(",")

    dept_count[dept] = dept_count.get(dept, 0) + 1

print(dept_count)
#
# Exercise 6 — CSV File (Sales Dataset)
#
# File: sales.csv
#
# product,quantity,price
# Laptop,5,75000
# Mouse,20,500
# Keyboard,15,1500
# Laptop,3,75000
# Mouse,10,500
#
# Questions
with open("sales.csv", "r") as file:
    lines = file.readlines()[1:]
# 1. Calculate total sales revenue.
total_revenue = 0

for line in lines:
    product, qty, price = line.strip().split(",")
    total_revenue += int(qty) * int(price)

print("Total Revenue:", total_revenue)

# 2. Find total quantity sold per product.
qty_per_product = {}

for line in lines:
    product, qty, price = line.strip().split(",")
    qty_per_product[product] = qty_per_product.get(product, 0) + int(qty)

print(qty_per_product)

# 3. Find the product with highest sales.
revenue_per_product = {}

for line in lines:
    product, qty, price = line.strip().split(",")
    revenue = int(qty) * int(price)
    revenue_per_product[product] = revenue_per_product.get(product, 0) + revenue

top_product = max(revenue_per_product, key=revenue_per_product.get)

print("Highest Sales Product:", top_product)

# 4. Calculate total revenue per product.
print(revenue_per_product)
# 5. Print products with sales above 50,000.
for product, revenue in revenue_per_product.items():
    if revenue > 50000:
        print(product)

#
# Bonus Challenge
#
# Using the sales.csv file:
# Write Python code to produce this output:
#
# Product Sales Summary
# Laptop → Qty: 8 Revenue: 600000
# Mouse → Qty: 30 Revenue: 15000
# Keyboard → Qty: 15 Revenue: 22500
summary = {}

for line in lines:
    product, qty, price = line.strip().split(",")

    qty = int(qty)
    price = int(price)
    revenue = qty * price

    if product not in summary:
        summary[product] = {"qty": 0, "revenue": 0}

    summary[product]["qty"] += qty
    summary[product]["revenue"] += revenue

print("Product Sales Summary")

for product, data in summary.items():
    print(f"{product} → Qty: {data['qty']} Revenue: {data['revenue']}")