s = "PAYPALISHIRING"
numRows = 3
if numRows==1:
    print(s)
res = ''
for i in range(numRows):
    increment = (numRows - 1)*2
    for j in range(i, len(s), increment):
        res+=s[j]
        if (i>0 and  i<numRows-1 and j+increment - 2*i < len(s)):
            res+=s[j+increment - 2*i]
print(res)

