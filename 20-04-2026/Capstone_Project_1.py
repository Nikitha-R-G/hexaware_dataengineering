# Python Capstone Project
#
# E-Commerce Order Analytics System
#
# Objective
#
# Build a Python program that analyzes data from multiple sources:
# product catalog (JSON)
# customer orders (CSV)
# website visits (TXT)
# The program should generate a sales and customer report.
#
# Project Files
#
# 1 website_visits.txt
#
# Each line represents a visitor.
#
# Rahul
# Sneha
# Arjun
# Rahul
# Priya
# Sneha
# Rahul
# Karan
# Arjun
# Sneha
#
# 2 products.json
#
# {
# "products": [
# {"product_id": 101, "name": "Laptop", "price": 75000},
# {"product_id": 102, "name": "Mouse", "price": 500},
# {"product_id": 103, "name": "Keyboard", "price": 1500},
# {"product_id": 104, "name": "Monitor", "price": 12000}
# ]
# }
#
# 3 orders.csv
#
# order_id,customer,product_id,quantity
# 1,Rahul,101,1
# 2,Sneha,102,2
# 3,Arjun,103,1
# 4,Rahul,102,3
# 5,Priya,104,1
# 6,Sneha,101,1
# 7,Karan,103,2
# 8,Rahul,104,1
#
# Part 1 — Website Visit Analysis (TXT)
#
# Task 1
#
# Read website_visits.txt .


website=[]
with open("website_visits.txt","r") as file:
    for line in file:
        website.append(line.strip())
#
# Task 2
#
# Print all visitors.
print("Print all visitors.")
with open("website_visits.txt","r") as file:
    for line in file:
        print(line.strip())
#
# Task 3
#
# Find the total number of visits.
total_visits=0
with open("website_visits.txt","r") as file:
    for line in file:
        total_visits+=1
print("total_visits",total_visits)
#
# Task 4
#
# Find unique visitors using a set.
unique_visitors=set(website)
print("unique_visitors",unique_visitors)
# Task 5
#
# Count how many times each visitor came to the website.
visits={}
for w in website:
    if w in visits:
        visits[w]+=1
    else:
        visits[w] = 1
print("visits:",visits)
# Example expected structure:
#
# {
# "Rahul":3,
# "Sneha":3,
# "Arjun":2,
# "Priya":1,
# "Karan":1
# }
#
# Task 6
#
# Find the most frequent visitor.
print("the most frequent visitor is",max(visits,key=visits.get))

#
# Part 2 — Product Catalog Analysis (JSON)
#
# Task 7
#
# Read products.json .
import json
with open("products.json","r") as file:
    products=json.load(file)
print("products:",products)

#
# Task 8
#
# Print all product names and prices.
print("Print all product names and prices:")
for p in products["products"]:
    name=p["name"]
    price=p["price"]
    print(name,":",price)
# Task 9
#
# Store product information in a dictionary.
product_dict={}
for p in products["products"]:
    product_dict[p["product_id"]]={
        "name":p["name"],
    "price":p["price"]
    }
print("product information in a dictionary:")
print(product_dict)
# Example structure:
#
# {
# 101: {"name":"Laptop","price":75000},
#
# 102: {"name":"Mouse","price":500}
# }
#
# Task 10
#
# Find the most expensive product.
name=""
max_price=0
for pid,details in product_dict.items():
    if max_price<details["price"]:
        max_price=details["price"]
        expensive=details["name"]
print("the most expensive product is",expensive)
# Task 11
#
# Find the least expensive product.
name=""
min_price=100000
for pid,details in product_dict.items():
    if min_price>details["price"]:
        min_price=details["price"]
        expensive=details["name"]
print("the least expensive product:",expensive)
#
# Part 3 — Orders Analysis (CSV)
#
# Task 12
#
# Read orders.csv .
with open("orders.csv","r") as file:
    lines = file.readlines()
#
# Task 13
#
# Print each order.
order_dict={}
productid=0
quantity=0
for l in lines:
    i,n,p,q=l.strip().split(",")
    order_dict[i]={
        "name":n,
        "productid":p,
        "quantity":q
    }
print("order_dict:",order_dict)

#
# Task 14
#
# Calculate the total quantity sold per product.
sold_per_product={}
for id,details in order_dict.items():
    pid = details["productid"]
    qty = int(details["quantity"].strip())
    if pid in sold_per_product:
        sold_per_product[pid] += qty
    else:
        sold_per_product[pid] = qty
print("the total quantity sold per product",sold_per_product)


# Task 15
#
# Calculate total orders per customer.
orders_per_customer={}
for id,details in order_dict.items():
    name = details["name"]
    if name in orders_per_customer:
        orders_per_customer[name] += 1
    else:
        orders_per_customer[name] = 1
print("total orders per customer:",orders_per_customer)
# Expected structure:
#
# {
# "Rahul":3,
# "Sneha":2,
# "Arjun":1,
# "Priya":1,
# "Karan":1
# }
#
# Part 4 — Sales Calculation
#
# Using product prices and order quantities:
# Task 16
# Calculate revenue for each order.
revenue={}
for order_id,order_details in order_dict.items():
    pid = int(order_details["productid"])
    qty = int(order_details["quantity"].strip())
    price=product_dict[pid]["price"]
    revenue[order_id]=price*qty
print("revenue for each order",revenue)

#
# Task 17
#
# Calculate total revenue.
total_revenue=0
for order_id,order_details in order_dict.items():
    pid = int(order_details["productid"])
    qty = int(order_details["quantity"].strip())
    price=product_dict[pid]["price"]
    total_revenue+=price*qty
print("total_revenue",total_revenue)
#
# Task 18
#
# Calculate total revenue per product.
product_revenue={}
for order_id,order_details in order_dict.items():
    pid = int(order_details["productid"])
    qty = int(order_details["quantity"].strip())
    price=product_dict[pid]["price"]
    name=product_dict[pid]["name"]
    if name in product_revenue:
        product_revenue[name]+=price*qty
    else:
        product_revenue[name] = price * qty
print("total revenue per product:",product_revenue)
# Example output structure:
#
# {
# "Laptop":150000,
# "Mouse":2500,
# "Keyboard":4500,
# "Monitor":24000
# }
#
# Task 19
#
# Find the highest selling product by revenue.
print("the highest selling product by revenue",max(product_revenue,key=product_revenue.get))
#
# Part 5 — Customer Analysis
#
# Task 20
#
# Calculate total spending per customer.
customer_revenue={}
for order_id,order_details in order_dict.items():
    pid = int(order_details["productid"])
    qty = int(order_details["quantity"].strip())
    price=product_dict[pid]["price"]
    name=order_dict[order_id]["name"]
    if name in customer_revenue:
        customer_revenue[name]+=price*qty
    else:
        customer_revenue[name] = price * qty
print("total spending per customer:",customer_revenue)
#
# Task 21
#
# Find the highest spending customer.
print("the highest spending customer is",max(customer_revenue,key=customer_revenue.get))
# Task 22
#
# Find customers who spent more than ₹50,000.
print("customers who spent more than ₹50,000:")
for name,price in customer_revenue.items():
    if price>50000:
        print(name)
#
# Part 6 — Functions
#
# Create functions for:
#
# Task 23
#
# Load visits from TXT.
def visits():
    website_visits=[]
    with open("website_visits.txt","r") as file:
        for line in file:
            website_visits.append(line.strip())
    return website_visits

#
# Task 24
#
# Load product catalog from JSON.
def products():
    with open("products.json","r") as file:
        products=json.load(file)
    product_dict={}
    for p in products["products"]:
        product_dict[p["product_id"]]={
        "name":p["name"],
    "price":p["price"]
    }
    return product_dict

# Task 25
#
# Load orders from CSV.
def orders():
    with open("orders.csv","r") as file:
        lines=file.readlines()
    order_dict = {}
    productid = 0
    quantity = 0
    for l in lines:
        i, n, p, q = l.split(",")
        print(id, name, productid, quantity)
        order_dict[i] = {
            "name": n,
            "productid": p,
            "quantity": q
        }
    return order_dict


#
# Task 26
#
# Calculate product revenue.
def productRevenue():
    product_revenue = {}
    for order_id, order_details in order_dict.items():
        pid = int(order_details["productid"])
        qty = int(order_details["quantity"].strip())
        price = product_dict[pid]["price"]
        name = product_dict[pid]["name"]
        if name in product_revenue:
            product_revenue[name] += price * qty
        else:
            product_revenue[name] = price * qty
    return product_revenue
# Task 27
#
# Calculate customer spending.
def customerSpending():
    customer_revenue = {}
    for order_id, order_details in order_dict.items():
        pid = int(order_details["productid"])
        qty = int(order_details["quantity"].strip())
        price = product_dict[pid]["price"]
        name = order_dict[order_id]["name"]
        if name in customer_revenue:
            customer_revenue[name] += price * qty
        else:
            customer_revenue[name] = price * qty
    return customer_revenue
# Task 28
#
# Find top customer.
cr=customerSpending()
def topCustomer():
    print("the top customer is", max(cr, key=cr.get))
topCustomer()

#
# Part 7 — Data Structures
#
print("DS")
# Use:
# list → store orders

def load_orders(order_dict):
    orders = []

    for oid, details in order_dict.items():
        orders.append(details)

    return orders
orders_list = load_orders(order_dict)
# dictionary → store product prices
print("dictionary → store product prices",products())
product_prices = products()
# set → store unique visitors
print("set → store unique visitors",unique_visitors)
# tuple → represent (product_name, revenue) pairs
product_sales = []

for name, revenue in product_revenue.items():
    product_sales.append((name, revenue))

print("tuple → represent (product_name, revenue) pairs",product_sales)

def calculate_revenue(orders, product_prices):

    total_revenue = 0
    product_revenue = {}
    customer_spending = {}

    for order in orders:

        customer = order["name"]
        pid = int(order["productid"])
        qty = int(order["quantity"].strip())

        price = product_prices[pid]["price"]
        revenue = price * qty

        total_revenue += revenue

        # product revenue
        if pid in product_revenue:
            product_revenue[pid] += revenue
        else:
            product_revenue[pid] = revenue

        # customer spending
        if customer in customer_spending:
            customer_spending[customer] += revenue
        else:
            customer_spending[customer] = revenue

    return total_revenue, product_revenue, customer_spending
# -------- Calculate Revenues --------
total_revenue, product_revenue, customer_spending = \
    calculate_revenue(orders_list, product_prices)
#
# Part 8 — Final Report Generation
#
# Create a file called sales_report.txt.
def generate_report(visits, orders, product_prices,
                    total_revenue, product_revenue, customer_spending):

    unique_visitors = set(visits)

    top_customer = max(customer_spending,
                       key=customer_spending.get)

    with open("sales_report.txt","w",encoding="utf-8") as f:

        f.write("E-Commerce Sales Report\n")
        f.write(f"Total Website Visits: {len(visits)}\n")
        f.write(f"Unique Visitors: {len(unique_visitors)}\n")
        f.write(f"Total Revenue: {total_revenue}\n\n")

        f.write(f"Top Customer: {top_customer}\n")

        f.write("\nProduct Sales\n")

        for pid, revenue in product_revenue.items():
            pname = product_prices[pid]["name"]
            f.write(f"{pname} → {revenue}\n")
generate_report(
    website,
    orders_list,
    product_prices,
    total_revenue,
    product_revenue,
    customer_spending
)
# Example output:
#
# E-Commerce Sales Report
# Total Website Visits: 10
# Unique Visitors: 5
# Total Revenue: 181000
#
# Top Customer: Rahul
# Product Sales
# Laptop → 150000
# Mouse → 2500
# Keyboard → 4500
# Monitor → 24000
#
# Final Challenge
#
# Task 29
#
# Find visitors who visited but never ordered anything.
def visitors_no_orders(visits, orders):

    visit_set = set(visits)
    order_customers = set(o["name"] for o in orders)

    result = visit_set - order_customers

    print("Visited but never ordered:", result)
visitors_no_orders(website, orders_list)
#
# Task 30
#
# Find customers who ordered but never visited the website more than once.
def ordered_not_regular(visits, orders):

    visit_count = {}

    for v in visits:
        visit_count[v] = visit_count.get(v, 0) + 1

    order_customers = set(o["name"] for o in orders)

    result = []

    for customer in order_customers:
        if visit_count.get(customer,0) <= 1:
            result.append(customer)

    print("Ordered but visited once:", result)
ordered_not_regular(unique_visitors, orders_list)