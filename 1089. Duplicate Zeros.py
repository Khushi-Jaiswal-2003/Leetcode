arr =[1,0,2,3,0,4,5,0]
c_arr = arr.copy()
for i in range(len(c_arr)):
    if c_arr[i] == 0:
        arr.insert(i+1, 0)

print(arr)
