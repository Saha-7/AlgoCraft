def revStr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev

print(revStr("lkjhgf"))

# [::-1]