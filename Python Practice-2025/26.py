# Count Number of Digits in a String
n = input("Enter a String: ").lower()
count = 0
for i in n:
    if i.isdigit() == True:
        count += 1


if count > 0:
    print(f"The Count of Digits is {count}")
else:
    print("No Digits Present!")