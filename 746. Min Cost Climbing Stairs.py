cost = [10,15,20]
if len(cost)==2:
    print(min(cost))

count = [0]*len(cost)
print(count)

count[0]=cost[0]
count[1]=cost[1]
print(count)

for i in range(2, len(cost)):
    # print(i)
    count[i]= min(count[i-1], count[i-2])+cost[i]
    # print(count)
    print(min(count[i-1], count[i-2]))
    print(cost[i])
print(min(count[-1], count[-2]))