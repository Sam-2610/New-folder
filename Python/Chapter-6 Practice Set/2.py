""" Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.  """




print("*Enter Marks Between 1-100*")


eng  = int(input("Enter the marks of English out of 100:"))
math = int(input("Enter the marks of Maths out of 100:"))
phy  = int(input("Enter the marks of Physics out of 100:"))
chem  = int(input("Enter the marks of Chemistry out of 100:"))
cs  = int(input("Enter the marks of Computer Science out of 100:"))

Percentage_eng = eng /100 *100
Percentage_math = math /100 *100
Percentage_phy = phy /100 *100
Percentage_chem = chem/100 *100
Percentage_cs = cs /100 *100
Percentage_Total = (eng + math + phy + chem + cs) / 500 * 100

if Percentage_eng < 33:
    print(f"You have failed in English")
elif Percentage_math < 33:
    print("You have failed in Maths")
elif Percentage_phy < 33:
    print("You have failed in physics")
elif Percentage_chem < 33:
    print("You have failed in Chemistry")
elif Percentage_cs < 33:
    print("You have failed in Computer Science")
elif Percentage_Total < 40:
    print("You have failed in the overall exam")
else:
    print("You have passed the exam:")
    print(f"Your total percentage is {Percentage_Total}%")
    print(f"Your percentage in English is {Percentage_eng}%")
    print(f"Your percentage in Maths is {Percentage_math}%")
    print(f"Your percentage in Physics is {Percentage_phy}%")
    print(f"Your percentage in Chemistry is {Percentage_chem}%")
    print(f"Your percentage in Computer Science is {Percentage_cs}%")

