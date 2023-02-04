low = 1000
high = 12000
digit = "123456789"
count_low = len(str(low))
count_high = len(str(high))
result = []
for i in range(count_low, count_high+1):
    for j in range(0, 10-i):
        num=int(digit[j:j+i])
        print(num, i, j)
        if num>=low and num<=high:
            result.append(num)
print(result)









