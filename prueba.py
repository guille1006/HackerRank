
s=[[4, 8, 2],
[4, 5, 7],
[6, 1, 6]]


print(s)
square=[]
for i in range(3):
    square.append(s[0][i])
square.append(s[1][2])
for i in range(2, -1, -1):
    print(i)
    square.append([2][i])
square.append(s[1][0])

