# todo 1st method Brute force approach
x= 1
if x==0:
    print(0)
else:
    for i in range(x+1):
        if i*i==x:
            print(i)
            break
        # print(i)
        elif i*i>x:
            print(i-1)
            break

# todo 2nd method optimized approach (using Binary search)
def Binary_Search(x):
    left = 0
    right = x
    mid = (left+right)//2
    Found = False
    while (left<= right and not False):
        mid = (left+right)//2
        if mid*mid==x:
            Found=True
            # print(mid)
            break
        elif mid*mid<x:
            left=mid+1
        elif mid*mid>x:
            right=mid-1
    if Found==True:
        print(mid)
    else:
        print(right)

x= 1
Binary_Search(x)

