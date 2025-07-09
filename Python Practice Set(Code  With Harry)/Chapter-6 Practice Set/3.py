'''A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams.'''


message = input("Enter a string: ").lower()

spam_phrases = ["make a lot of money", "buy now", "subscribe this", "click this"]

is_spam = False
for phrase in spam_phrases:
    if phrase in message:
        is_spam = True
        break

if is_spam:
    print("This is a Spam Message")
else:
    print("This is not a Spam Message")




    