# Python Data Structures


# Exercise 1 – Remove Duplicates from a List

customers = [101,102,103,101,104,102,105]

# Tasks
# 1. Remove duplicate IDs
unique_customers=set(customers)

# 2. Print unique customers
print(unique_customers)

# 3. Print total number of unique customers
print(len(unique_customers))

# Exercise 2 – Frequency Counter

numbers = [10,20,10,30,20,10,40]

# Tasks
# 1. Count how many times each number appears
freq={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
# 2. Store the result in a dictionary
print(freq)
# Expected structure
# {10:3, 20:2, 30:1, 40:1}
#
# Exercise 3 – Student Marks Analyzer
#
students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}
#
# Tasks
# 1. Print the topper
print(max(students, key=students.get))
# 2. Print average marks
avg=sum(students.values())/len(students)
print(avg)
# 3. Print students scoring above 85
for student,mark in students.items():
    if mark>85:
        print(student)
#
# Exercise 4 – Inventory Management
#
inventory = {
"laptop":10,
"mouse":25,
"keyboard":15
}
#
# Tasks
# 1. Add "monitor":8
inventory["monitor"]=8
print(inventory)
# 2. Reduce laptop stock by 2
inventory["laptop"]=8
# 3. Print items with stock less than 10
for name,stock in inventory.items():
    if stock<10:
        print(name)
# Exercise 5 – Email Domain Extractor
#
emails = [
"user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]
#
# Tasks
# 1. Extract domains
domain=[]
for e in emails:
    d=e.split("@")[1]
    domain.append(d)
print(domain)

# 2. Count how many users per domain
dodict={}
for d in domain:
    if d in dodict:
        dodict[d]+=1
    else:
        dodict[d]=1
print(dodict)
# Expected output
#
# {
# "gmail.com":2,
# "yahoo.com":1,
# "outlook.com":1
# }
#
# Exercise 6 – Common Students in Two
# Classes
#
classA = {"Rahul","Sneha","Amit","Neha"}
classB = {"Sneha","Amit","Karan","Riya"}
#
# Tasks
# 1. Students in both classes
result_intersection=classA.intersection(classB)
print(result_intersection)

# 2. Students only in Class A
result_difference=classA.difference(classB)
print(result_difference)

# 3. All unique students
result_union=classA.union(classB)
print(result_union)

# Exercise 7 – Product Price Update
#
products = {
"Laptop":75000,
"Mobile":30000,
"Tablet":25000
}
#
# Tasks
# 1. Increase all prices by 10%
for item,price in products.items():
    products[item]=price+((10/100)*price)
# 2. Print updated prices
print(products)

# Exercise 8 – Word Counter
#
# Given a sentence
#
sentence = "python is easy and python is powerful"
#
# Tasks
# 1. Count frequency of each word
words=sentence.split()
print(words)

# 2. Store results in dictionary
word_count={}
for i in words:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
print(word_count)
# Expected output
#
# {
# "python":2,
# "is":2,
# "easy":1,
# "and":1,
# "powerful":1
# }
#
# Exercise 9 – Highest Selling Product
#
sales = [
{"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]
#
# Tasks
# 1. Calculate total sales per product
total_sales = {}

for item in sales:
    product = item["product"]
    qty = item["qty"]

    if product in total_sales:
        total_sales[product] += qty
    else:
        total_sales[product] = qty

print(total_sales)
# 2. Find highest selling product
print(max(total_sales), key=total_sales.get)
# Exercise 10 – User Login Tracker
#
logins = [
("Rahul","10:00"),
("Sneha","10:10"),
("Rahul","11:00"),
("Arjun","11:15"),
("Sneha","11:30")
]
#
# Tasks
# 1. Count how many times each user logged in
login_count={}
for i in logins:
    j=i[0]
    if j in login_count:
        login_count[j]+=1
    else:
        login_count[j]=1

# 2. Store results in dictionary
print(login_count)
# Expected output
#
# {
# "Rahul":2,
# "Sneha":2,
# "Arjun":1
# }
#
# Final Challenge
#
# Exercise 11 – E-commerce Order Analysis
#
orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]
#
# Tasks
# 1. Calculate total spending per customer
total_spending = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]

    if customer in total_spending:
        total_spending[customer] += amount
    else:
        total_spending[customer] = amount

print(total_spending)
# 2. Find highest spending customer
highest_customer = max(total_spending, key=total_spending.get)

print("Highest Spending Customer:", highest_customer)
print("Amount Spent:", total_spending[highest_customer])
# 3. Count total orders per customer
order_count = {}

for order in orders:
    customer = order["customer"]
    order_count[customer] = order_count.get(customer, 0) + 1

print(order_count)
