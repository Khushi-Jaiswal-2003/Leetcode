class Solution:

    def comb(self,ind, arr, target, ans, ds, n):
        if ind==n:
            if target==0:
                ans.append(ds[:])
            return

        if arr[ind]<=target:
            ds.append(arr[ind])
            self.comb(ind, arr, target-arr[ind], ans, ds, n)
            ds.pop()

        self.comb(ind+1, arr, target, ans, ds, n)


    def combinationSum(self, candidates,target):
        ans = []
        n = len(candidates)
        a = self.comb(0, candidates, target, ans, [], n)
        return ans

cl = Solution()
print(cl.combinationSum([2,3,6,7], 7))



