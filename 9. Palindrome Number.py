class Solution:
    def pal(self, i, x, n):
        if i>=n/2:
            return True
        if x[i]!=x[n-i-1]:
            return False
        else:
            return self.pal(i+1, x, n)
    def isPalindrome(self, x):
        x = str(x)
        ans = self.pal(0, x, len(x))
        return ans

a = Solution()
print(a.isPalindrome(-121))


