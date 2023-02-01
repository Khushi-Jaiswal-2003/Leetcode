# todo pending....
arr =  [0,3,2,1]
index = 1
n =len(arr)
if len(arr)<3:
    print(False)
else:
    left = arr[0]
    mid = arr.index(max(arr))
    right = arr[-1]
    print(left, mid, right)
    count_left = 0
    for i in range(mid):
        # print(arr[i])
        if left<arr[i]:
            count_left+=1
        else:
            count_left-=1
    print(count_left)

class Solution:
    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False

        ans = 0

        for i in range(len(arr) - 1):

            if (arr[i] < arr[i + 1]) and (ans == 0 or ans == 1):
                ans = 1

            elif (arr[i] > arr[i + 1]) and (ans == 1 or ans == 2):
                ans = 2

            else:
                return False

        if ans == 2:
            return True
        else:
            return False

