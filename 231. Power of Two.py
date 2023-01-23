n = -16
count=1
if n<0:
    print(False)
else:
    while (n>1):
        if n%2!=0:
            count=0
        n//=2
    if count==1:
        print(True)
    else:
        print(False)