from collections import Counter

s = "cbacdcbc"
freq = Counter(s)
ans = []
print(freq)
sort_freq = sorted(set(freq.values()))
print(sort_freq)
for i in range(len(sort_freq)):
    for x, y in freq.items():
        if sort_freq[i]==y:
            print(x, y)


