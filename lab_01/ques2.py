#write a python code to assign grade

s1 = int(input("Enter marks for subject1 (out of 100):"))
s2 = int(input("Enter marks for subject2 (out of 100):"))
s3 = int(input("Enter marks for subject3 (out of 100):"))
s4 = int(input("Enter marks for subject4 (out of 100):"))
s5 = int(input("Enter marks for subject5 (out of 100):"))

totalmarks= s1+ s2+ s3+ s4+ s5
percentage= (totalmarks/500)*100

if percentage>= 90:
    grade= "A+"

elif percentage>= 80 and percentage<90:
    grade= "A"

elif percentage>= 70 and percentage<80:
    grade= "B+"

elif percentage>= 60 and percentage<70:
    grade= "B"

elif percentage>= 50 and percentage<60:
    grade= "C"

elif percentage>= 40 and percentage<50:
    grade= "D"

elif percentage>= 35 and percentage<40:
    grade= "E"

else:
    grade= "F"

print("Grade is:")
print(grade)