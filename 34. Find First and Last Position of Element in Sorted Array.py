# nums = [5,7,7,8,8,10]
# target = 8
# left = 0
# right = len(nums)-1
# mid = (left+right)//2
# Found = False
# while(left<right and not Found):
#     mid = (left + right) // 2
#     if nums[mid]==target:
#         print(mid)
#         Found=True
#     elif nums[mid]<target:
#         left=mid+1
#     else:
#         right = mid-1
class Solution:

    def searchRange(self, nums, target):

        ans = [-1,-1]
        start = self.findIndex(nums,target,True)
        end = self.findIndex(nums,target,False)

        ans[0] = start
        ans[1] = end
        return ans

    def findIndex(self, nums, target, boolean):

        start = 0
        end = len(nums) - 1
        ans = -1

        while (start <= end):
            mid = start + (end - start) // 2

            if (target > nums[mid]):
                start = mid + 1

            if (target < nums[mid]):
                end = mid - 1

            if(target == nums[mid]):
                ans = mid
                if(boolean==True):
                    end = mid-1
                else:
                    start = mid+1
        return ans
