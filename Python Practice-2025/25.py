# Count Number of Occurrences of a Character in a String
n = input("Enter a String: ").lower()
x = input("Enter the Character you want to Count: ").lower()
count = 0

for i in n:
    if i == x:
        count += 1

if count > 0:
    print(f"The Count of Occurrence of '{x}' is: {count}")
else:
    print(f"The Character '{x}' is not in the String.")
