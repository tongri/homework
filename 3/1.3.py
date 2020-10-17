a = []
with open ("1.3.py", "r") as f:
    for line in f:
        a.append(line)
a = reversed(a)
print("".join(a))