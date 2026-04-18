# set:
# 1) dont allow duplicate value
numbers={1,2,2,5,7,8,9}
print(numbers)

# list:set(to create unique list
list=[1,2,22,34,55,1,2]
unique_list=set(list)
print(unique_list)

# add[ to add only one element]
numbers.add(90)
print(numbers)

# update[ to add multiple elements into set using list
numbers.update([20,5,2005])
print(numbers)

# set operations
set1={10,20,30}
set2={30,40,50}

# 1.union(combine both set and return unique values)
result_union=set1.union(set2)
print(result_union)

# 2.difference(return unique values in set1 after comparing both)
# set1- unique
result_difference=set1.difference(set2)
print(result_difference)
#
# set2-unique
result_difference=set2.difference(set1)
print(result_difference)

# 3.intersection(commmon element in both set)
result_intersection=set1.intersection(set2)
print(result_intersection)
