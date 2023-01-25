
# s = "aaaaaa"
# t = "bbaaaa"
# list_ans = []
# for i in s:
#     x = t.find(i)
#     list_ans.append(x)
# print(list_ans)
# count = 0
# if -1 in list_ans:
#     print(False)
# else:
#     if list_ans== sorted(list_ans):
#         count=1
#
#     if count==1:
#         print(True)
#     else:
#         print(False)

s = "abc"
t = "abcj"
for i in s:
    if i in t:
        t = t[t.index(i)+1:]
        print(t)
