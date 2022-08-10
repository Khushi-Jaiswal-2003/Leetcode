n = 5
if n==1:
    print([[1]])
elif n==2:
    print([[1], [1, 1]])

list = []
list.append([1])
list.append([1, 1])
print(list)
count =[1, 1]
for i in range(2, n):
    nested_list =[]
    nested_list.insert(0, 1)
    nested_list.insert(i, 1)
    print(nested_list)
    for k in range(1, i):
        nested_list.insert(k, count[k-1]+count[k])
    list.append(nested_list)
    count=nested_list
print(list)