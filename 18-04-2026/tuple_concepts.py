# tuple:
# 1.dont allow modify data
# 2.can store different type of data
numbers=(1,2,3,4,5)
print(numbers)

friends=("niki","praki","tharun")
print(friends)

# index access
print(friends[0])
print(numbers[-1])

# slicing
print(friends[1:2])

# len
print(len(friends))

# loop
for i in friends:
    print(i)

# modify:cant happen because it is tuple it doent allow it
# numbers[1]=10
# print(numbers)

# packing
student=("Niki",20,450000,"AI")
print(student)

# unpacking
name,age,fee,course=student
print(name)
print(age)
print(fee)
print(course)

