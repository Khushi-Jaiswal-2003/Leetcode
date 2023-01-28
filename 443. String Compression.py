chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
copy_chars = chars.copy()

chars.clear()
set_char = list(set(copy_chars))
for i in range(len(copy_chars)):
    x = ''
    if copy_chars[i] in chars:
        pass
    else:
        if copy_chars.count(copy_chars[i])==1:
            chars.append(copy_chars[i])
        else:
            chars.append(copy_chars[i])
            x+=str(copy_chars.count(copy_chars[i]))
            x=list(x)
            print(x)
            chars.extend(x)
print(chars)