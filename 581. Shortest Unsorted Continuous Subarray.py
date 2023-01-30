nums = [2,6,4,8,10,9,15]

is_same= [a==b for a, b in zip(nums, sorted(nums))]

print(is_same)

# print(all(is_same))
if nums == sorted(nums):
    print(0)
else:
    if all(is_same):
        print(all(is_same))

    else:
        # print(len(nums), is_same.index(False), is_same[::-1].index(False))
        print(len(nums)-is_same.index(False)-is_same[::-1].index(False))