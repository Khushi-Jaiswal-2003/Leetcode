s = "RLRRLLRLRL"
r_count = 0
l_count = 0
output = 0
for c in s:
    if c == "R":
        r_count += 1
    else:
        l_count += 1
    if r_count == l_count:
        output += 1
        r_count = 0
        l_count = 0
print(output)