# read and print
with open("data.txt","r") as file:
    for line in file:
        print(line.strip())

# read and store value
with open("data.txt","r") as file:
    students=file.readline()
print("Total students:",len(students))

# op with numeric data
total=0
with open("datanum.txt","r") as file:
    for line in file:
        total+=int(line.strip())
print(total)

# write - overwrite(exixting data vanished new data updated
with open("data.txt","w") as file:
    file.write("Niki\n")
    file.write("Praki\n")
    file.write("Tharun\n")

# append-add data at end of file not overwrite
with open("data.txt","a") as file:
    file.write("Gnanavel\n")
    file.write("Vanitha\n")
    file.write("Tamizharasi\n")

# write lines
languages=["Python\n","Java\n","C++\n","I am very happy!!!!!"]
with open("data.txt","w") as file:
    file.writelines(languages)

import json
# read json file
with open("data2.json","r") as file:
    data=json.load(file)
print(data)

# print data
for student in data["students"]:
    print(student["name"],student["marks"])

# write json
students={"students":[{"name":"Priya","marks":88},
                      {"name":"Karan","marks":75}]}
# indent to get a preety op
with open("output.json","w") as file:
    json.dump(students,file,indent=4)

import csv
# read csv
with open("data3.csv","r") as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)

# read as dictioanry
with open("data3.csv","r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        print(row["name"],row["marks"])

# write in csv
data=[["name","marks"],
      ["Priya",99],
      ["Karan",78]]

with open("outputcsv.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)
