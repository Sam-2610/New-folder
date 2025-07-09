""" Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50        
=> F """



marks = int(input("Enter the marks: "))

if 90 <= marks <= 100:
    print("Excellent")
elif 80 <= marks < 90:
    print("A Grade")
elif 70 <= marks < 80:
    print("B Grade")
elif 60 <= marks < 70:
    print("C Grade")
elif 50 <= marks < 60:
    print("D Grade")
else:
    print("Fail")
