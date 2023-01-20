num = [1, 3, 5, 6]
target = 8
# for i in range(len(num) - 1):
#     if num[i]<target and num[i + 1]>target:
#         num.insert(i + 1, target)
# if num[-1]<target:
#     num.insert(len(num), target)
# elif num[0]>target:
#     num.insert(0, target)
# for i in range(len(num)):
#     if num[i] == target:
#         print(i)
left = 0
right = len(num)-1
mid = (left+right)//2
while(left<=right):
    mid = (left+right)//2
    if num[mid]==target:
        print(mid)
    elif num[mid]<target:
        left=mid+1
    else:
        right=mid-1
if num[mid]>=target:
    print(mid)
else:
    print(mid+1)