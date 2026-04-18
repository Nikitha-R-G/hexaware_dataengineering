
# dictionary:key-value pairs
student={"name":"Niki",
         "age":22,
         "course":"AI"}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])

# get
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

# add new pair
student["city"]="Hyderabad"
print(student)