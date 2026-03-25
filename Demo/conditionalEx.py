print()
Marks1 = float(input("Enter the marks of the first subject: "))
print()

Marks2 = float(input("Enter the marks of the second subject:"))
print()

Marks3 = float(input("Enter the marks of the third subject: "))


average = (Marks1 + Marks2 + Marks3) / 3
print()

print("Your Average is: %.2f " %(average))
print()

if (average >=90 and Marks1 >=50 and Marks2 >=50 and Marks3 >=50):
    print("Grade: A")
    print()

elif (average >=80 and Marks1 >=50 and Marks2 >=50 and Marks3 >=50):
    print("Grade: B")
    print()

elif (average >=70 and Marks1 >=50 and Marks2 >=50 and Marks3 >=50):
    print("Grade: C")
    print()

elif (average >=60 and Marks1 >=50 and Marks2 >=50 and Marks3 >=50):
    print("Grade: D")
    print()

elif (average >=50 and Marks1 >=50 and Marks2 >=50 and Marks3 >=50):
    print("Grade: E")
    print()

else:
    print("Try next time you are fail ")
    print()
    



                     