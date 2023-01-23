# def check_num(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             # print(i)
#             count += 1
#     if count == 2:
#         return (n)
#
#
# class Solution:
#     def countPrimes(n):
#         occur = 0
#         for i in range(1, n):
#             if check_num(i)==None:
#                 pass
#             else:
#                 occur+=1
#                 # print(check_num(i))
#         return(occur)
# n = 47
# x = Solution.countPrimes(n)
# print(x)

n =10
seen, ans = [0] * n, 0
for num in range(2, n):
    if seen[num]:
        print(seen[num])
        continue
    ans += 1
    seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
print(ans)