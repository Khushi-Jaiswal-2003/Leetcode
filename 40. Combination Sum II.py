class Solution:
    def comb(self, ind, arr, target, ans, ds, n):
        if target==0:
            ans.append(ds[:])
            return

        for i in range(ind, n):
            if i>ind and arr[i]==arr[i-1]:
                continue

            if arr[i]>target:
                break

            ds.append(arr[i])
            self.comb(i+1, arr, target-arr[i], ans, ds, n)
            ds.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        n = len(candidates)
        a = self.comb(0, candidates, target, ans, [], n)
        print(ans)



