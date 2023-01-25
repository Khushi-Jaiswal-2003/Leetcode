ransomNote = "aca"
magazine = "aabc"
pop_magazine = []
magazine = list(magazine)
for i in ransomNote:
    if i in magazine:
        r= magazine.pop(magazine.index(i))
        pop_magazine.append(r)
        print(magazine)
print(pop_magazine)
if len(pop_magazine)==len(ransomNote):
    print(True)
else:
    print(False)

