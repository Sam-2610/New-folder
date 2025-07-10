# Count Vowels in String
s = input("Enter a String: ").lower()
count = 0
for i in s:
    if i in ["a","e","i","o","u"]:
        count += 1

if count > 1:
    print(f"The Count of Vowel in String : {count}")
else:
    print("No Vowles in String!")