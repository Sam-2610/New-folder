""" . Write a program to input name, marks and phone number of a student and format it 
using the format function like below: 
“The name of the student is Harry, his marks are 72 and phone number is 99999888” """

Name = input("Enter Your Name: ")
Marks = int(input("Enter Your Marks: "))
PhNo = int(input("Enter Your Phone No.: "))

print("The name of the student is {}, his marks are {} and phone number is {}".format(Name,Marks,PhNo))