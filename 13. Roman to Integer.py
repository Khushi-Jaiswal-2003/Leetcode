s = input()
num = 0
dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for i in range(len(s)):
    if i + 1 != len(s) and dict_roman[s[i]] < dict_roman[s[i + 1]]:
        print(i+1, len(s))
        print(dict_roman[s[i]], dict_roman[s[i + 1]])

        num = num - dict_roman[s[i]]
        print(num)
    else:
        num = num + dict_roman[s[i]]
        print(num)
print(num)
