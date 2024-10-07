#1---------------------------------------------------------------------------------------------------
def solveMeFirst(a,b):
	return a+b
#2---------------------------------------------------------------------------------------------------
def simpleArraySum(ar):
    return sum(ar)
#3---------------------------------------------------------------------------------------------------
def compareTriplets(a, b):
    sol=[0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            sol[0]+=1
        elif a[i]<b[i]:
            sol[1]+=1
    return sol
#4---------------------------------------------------------------------------------------------------
def diagonalDifference(arr):
    sol=0
    print(arr)
    for i in range(len(arr)):
        sol+=arr[i][i]-arr[i][len(arr)-i-1]
    return abs(sol)
#5---------------------------------------------------------------------------------------------------
def plusMinus(arr):
    sol=[0,0,0]
    suma=1/len(arr)
    for i in range(len(arr)):
        if arr[i]>0:
            sol[0]+=suma
        elif arr[i]<0:
            sol[1]+=suma
        else:
            sol[2]+=suma
    for valor in sol:
        valor=str(float(valor))
        print(valor[:valor.index('.')+7])
#6---------------------------------------------------------------------------------------------------
def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)
#7---------------------------------------------------------------------------------------------------
def miniMaxSum(arr):
    maximos=arr[:]
    minimos=arr[:]
    minimo=0
    maximo=0
    for _ in range(len(arr)-1):
        minimo+=minimos.pop(minimos.index(min(minimos)))
        maximo+=maximos.pop(maximos.index(max(maximos)))
    print(minimo,maximo)
    return minimo, maximo
#8---------------------------------------------------------------------------------------------------
def birthdayCakeCandles(candles):
    tallest=max(candles)
    return candles.count(tallest)
#9---------------------------------------------------------------------------------------------------
def timeConversion(s):
    hora=(s[-2:])
    if hora=="PM" and s[:2]!="12":
        hora_nueva=str(int(s[:2])+12)
        s=hora_nueva+s[2:]
    elif hora=="AM" and s[:2]=="12":
        s="00"+s[2:]
    return s[:-2]

#10---------------------------------------------------------------------------------------------------
def gradingStudents(grades):
    solucion=[]
    for i in grades:
        if i<38:
            solucion.append(i)
        elif i%5>2:
            solucion.append((i//5)*5+5)
        else: 
            solucion.append(i)
    return solucion
#11---------------------------------------------------------------------------------------------------
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_landed=0
    oranges_landed=0
    for i in apples:
        landed=i+a
        if landed>=s and landed<=t:
            apples_landed+=1
    print(apples_landed)
    for i in oranges:
        landed=i+b
        if landed>=s and landed<=t:
            oranges_landed+=1
    print(oranges_landed)
#12---------------------------------------------------------------------------------------------------
def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        return "NO"
    while x1<=100000000 and x2<=100000000:
        x1+=v1
        x2+=v2
        if x1==x2:
            return "YES"
    return "NO"
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
