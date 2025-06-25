s = "Data Structures and Algorithm"

# Positive Indexing
q = s[0]
print(q)

# Negative Indexing
w = s[-1]
print(w)

# Slicing

e = s[1:6]
print(e)

# Editing

r = "S" + s[1:]
print(r)

# Addition

t = "Hello" + "World"
print(t)

# Multiplication

y = s*2
print(y)

# Relational Operators

print("hello" == "earld") # type: ignore

# Logical Operators
u = "Hello" and "world"
o = "hello" or "world"
p = "" and "World"
a = "hello" or ""

print(u)
print(o)
print(p)
print(a)

# Membership Operators


if "a" in s.lower():
    print("true")

# length

d = len(s)
print(d)

# min/max
print(min(s))
print(max(s))

# Sorted
f = sorted(s)
print(f)

# Capitalize/Title
print(s.capitalize())
print(s.title())

# Upper/Lower/Swapcase

print(s.upper())
print(s.lower())
print(s.swapcase())

# Find/Index

print(s.find("t"))
print(s.index("a"))

# Endswith/Startswith

print(s.startswith("Data"))
print(s.startswith("m"))

# isalnum/isalpha/isdigit

print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

# split

c = s.split(".")
print(c)

# Join

b = s.join("")
print(b)

# Replace

n = s.replace("a","d")
print(n)

# Strip

h = s.strip()
print(h)