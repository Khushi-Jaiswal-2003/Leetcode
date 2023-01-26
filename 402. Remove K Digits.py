num = "112"
k = 1
st = []
for i in num:
    while k and len(st) > 0 and st[-1] > i:
        k -= 1
        st.pop()
    st.append(i)
while k:
    k -= 1
    st.pop()
st = "".join(st).lstrip("0")
print(st) if st else "0"