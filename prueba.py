def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        return "NO"
    while x1<=1000000 and x2<=1000000:
        x1+=v1
        x2+=v2
        print(x1,x2)
        if x1==x2:
            return "YES"
    return "NO"
print(kangaroo(4602,8519,7585,8362))