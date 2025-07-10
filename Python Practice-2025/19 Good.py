# Iterate through two lists in Parallel

l = [i for i in range(1, 11)]
l2 = [x for x in range(11, 21)]

for a, b in zip(l, l2):
    print(f"{a}  {b}")
