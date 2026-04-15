mark=int(input("Enter your marks:"))

if mark>=90:
    print("Grade A")
elif 89>=mark>=70:
    print("Grade B")
elif 50<=mark<=69:
    print("Grade C")
else:
    print("Fail")