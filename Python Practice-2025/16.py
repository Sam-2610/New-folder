# Remove Puncutations

s = "hello.www!"
result = ""
for i in s.lower():
    if i not in ['!', ',', '.', '?']:
        result += i

print(result)
