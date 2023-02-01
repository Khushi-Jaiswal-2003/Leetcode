pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
index, stack = 0, []
for p in pushed:
    stack.append(p)
    # print(stack)
    while stack and stack[-1] == popped[index]:
        print(stack, stack[-1], popped[index])
        stack.pop()
        index += 1
print(not stack)