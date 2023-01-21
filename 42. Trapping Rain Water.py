height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [8, 8, 2, 4, 5, 5, 1]
copy_height = height.copy()
x = copy_height[::-1]
print(x)
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        x[i+1]=x[i]
    if height[i]>height[i+1]:
        height[i+1]=height[i]
print(x, height)
x = x[::-1]
d = []
for i in range(len(x)):
    d.append(min(height[i], x[i]))
print(d)
for i in range(len(d)):
    d[i]=d[i]-copy_height[i]
    print(d)
print(sum(d))