moves = "UDRl"
count_1= 0
count_2=0
for i in moves:
    if i=="U":
        count_1+=1
    elif i=="R":
        count_2+=1
    elif i=="D":
        count_1-=1
    else:
        count_2-=1
if count_1==0 and count_2==0:
    print(True)
else:
    print(False)
