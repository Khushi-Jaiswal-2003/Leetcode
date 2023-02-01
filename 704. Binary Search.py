nums =  [-1,0,3,5,9,12]
target = 2
left = 0
right = len(nums)-1
mid = (left+right)//2
Found = False
while(left<=right and not Found):
    mid = (left+right)//2
    if nums[mid]==target:
        Found=True
    elif nums[mid]<target:
        left = mid+1
    else:
        right=mid-1
if Found==True:
    print(mid)
else:
    print(-1)
