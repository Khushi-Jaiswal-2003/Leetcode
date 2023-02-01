s = "abcde"
goal = "abced"
if len(s)==len(goal):
    for i in range(len(s)):
        if s[i]==goal[0]:
            if s[i:]+s[:i]==goal:
                print(True)
    else:
        print(False)
else:
    print(False)
