# Check if a String is palindrome or not
x = input("Enter a String: ")
rev = x[::-1]
if rev == x:
    print(f"The String {x} is Palindrome!")
else:
    print(f"The String {x} is Not Palindrome!") 