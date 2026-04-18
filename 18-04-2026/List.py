

numbers=[10,20,30,40,50]
print(numbers)

fruits=["apple","banana","orange","mango","papaya"]
print(fruits)

# index access
print(numbers[0])
print(fruits[-1])

# modify elements
fruits[-1]="Watermelon"
print(fruits)

# add an elemenet
fruits.append("Grapes")
print(fruits)

# insert
numbers.insert(5,100)
print(numbers)

# remove
numbers.remove(100)
print(numbers)

# remove last element
numbers.pop()
print(numbers)

# length of list
print(len(numbers))

# loop in list
for i in numbers:
    print(i)

# check element present in list or not
if "banana" in fruits:
    print("banana in list!!")
if "papaya" not in fruits:
    print("papaya not present...")

# slicing
print(fruits[0:2])

# reverse
fruits.reverse()
print(fruits)

# sort
numbers.sort()
print(numbers)

# operations
print(max(numbers))
print(min(numbers))
print(sum(numbers))

