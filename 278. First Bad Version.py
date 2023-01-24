n = 6
version = ['a', 'a', 'b', 'b', 'b', 'b']
left =0
right = len(version)-1
mid = (left+right)//2
while(left<right):
    mid=(left+right)//2
    if version[mid]:
        right=left
    else:
        left=mid-1
print(left)