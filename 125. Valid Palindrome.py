

class Solution:
    def pal(self,i, ans, n):
        if i>=n/2:
            return True
        if ans[i]!=ans[n-i-1]:
            return False
        else:
            return self.pal(i+1, ans, n)

    def isPalindrome(self, s):
        ans = ''
        for i in s:
            if i.isupper():
                ans += i.lower()
            elif i.islower():
                ans += i
        c = self.pal(0, ans, len(ans))
        return c


a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))

