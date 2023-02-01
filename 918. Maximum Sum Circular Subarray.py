# todo code done but not in pycharm
cs = 0
a = [5,-3,5]
for i in range(len(a)):
    cs+= a[i]
    a[i]= -a[i]



def Kadane(nums):
    cursum, maxsum = nums[0], nums[0]
    for i in nums[1:]:
        cursum=max(i, cursum+i)
        maxsum=max(cursum, maxsum)
    return maxsum


print(Kadane(a))

