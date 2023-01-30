word = "USA"
count =0
if word[0].isupper():
    for i in word:
        if i.isupper():
            count+=1
    if len(word) == count:
        print(True)
    elif count == 1:
        print(True)
    else:
        print(False)
else:
    for i in word:
        if i.islower():
            count+=1
    if count==len(word):
        print(True)
    else:
        print(False)


