s1 = "ab"
s2 = "eidbaooo"
if len(s1)>len(s2): print(False)

s1count, s2count = [0]*26, [0]*26

for i in range(len(s1)):
    s1count[ord(s1[i])-ord('a')]+=1
    s2count[ord(s2[i])-ord('a')]+=1

print(s1count, s2count)

matches = 0
for i in range(26):
    matches+=(1 if s1count[i]==s2count[i] else 0)
    # print(matches)

l = 0
for i in range(len(s1),len(s2)):
    if matches==26: print(True)
    index = ord(s2[i])-ord('a')
    s2count[index]+=1

    if s1count[index]==s2count[index]:
        matches+=1

    elif s1count[index]+1 == s2count[index]:
        matches-=1

    index = ord(s2[l])-ord('a')
    s2count[index]-=1

    if s1count[index]==s2count[index]:
        matches+=1

    elif s1count[index]-1 == s2count[index]:
        matches-=1
    l+=1
print(matches==26)

s1 = "ab"
s2 = "eidbaooo"
if len(s1) > len(s2):
    print( False)

# map of charactar to an index in range a-z.
s1count = [0] * 26
s2count = [0] * 26

for i in range(len(s1)):
    index = ord(s1[i]) - ord('a')
    index2 = ord(s2[i]) - ord('a')
    s1count[index] = s1count[index] + 1
    s2count[index2] = s2count[index2] + 1
matches = 0
for index in range(26):
    if s1count[index] == s2count[index]:
        matches = matches + 1

left = 0
for right in range(len(s1), len(s2)):  # start after initial window sized to len(s1)
    if matches == 26:
        print( True)

    # update indexes for character that was added on right
    index = ord(s2[right]) - ord('a')
    s2count[index] = s2count[index] + 1  # update character for s
    if s1count[index] == s2count[index]:
        # now they are equal
        matches = matches + 1
    elif s1count[index] + 1 == s2count[index]:
        # they were equal, but now they are not equal anymore
        matches = matches - 1

    # update indexes for character that was added on left
    index = ord(s2[left]) - ord('a')
    s2count[index] = s2count[index] - 1
    if s1count[index] == s2count[index]:
        matches = matches + 1
    elif s1count[index] - 1 == s2count[index]:
        matches = matches - 1

    # update left window
    left = left + 1

print( matches == 26)