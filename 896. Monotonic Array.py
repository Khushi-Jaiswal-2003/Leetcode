nums = [1,2,2,3]
if nums == sorted(nums):
    print(True)
elif nums==sorted(nums)[::-1]:
    print(True)
else:
    print(False)