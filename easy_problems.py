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
#13---------------------------------------------------------------------------------------------------
def getTotalX(a, b):#Este esta un poquito clunky pero resuelve
    #Lo primero que hago es ver si los del grupo a son factores de los del grupo b
    for i in a:
        for j in b:
            if j%i!=0:
                return 0
            
    #Ahora lo que hago es quitar del grupo a los valores que ya son factores de un numero mayor
    for i in a[::-1]:
        for j in a[:]:
            if i==j:
                pass
            elif i%j==0:
                a.pop(a.index(j))

    #Multiplico todos los elementos del grupo a
    numero=1
    for i in a:
        numero=numero*i

    #Creo un array con todos los posibles elementos que en un principio podrian ser solucion
    posibles_numeros=[]
    i=1
    numero_base=numero
    numeros_base=[numero_base]
    numeros_base+=a
    for we in numeros_base:
        wee=we
        while wee<=min(b):
            posibles_numeros.append(wee)
            i+=1
            wee=we*i
            print(posibles_numeros, wee)
    #Compruebo si son solucion
    for i in posibles_numeros[:]:
        for j in b:
            if j%i!=0:
                posibles_numeros.pop(posibles_numeros.index(i))
                break
    for i in posibles_numeros[:]:
        for j in a:
            if i%j!=0:
                posibles_numeros.pop(posibles_numeros.index(i))
                break

    posibles_numeros=list(set(posibles_numeros))
    print(posibles_numeros)
    return len(posibles_numeros)
#14---------------------------------------------------------------------------------------------------
def breakingRecords(scores):
    minimo=10000000000000
    maximo=-1
    score_minimo=-1
    score_maximo=-1
    for i in scores:
        if i <minimo:
            minimo=i
            score_minimo+=1
        if i >maximo:
            maximo=i
            score_maximo+=1
    return [score_maximo,score_minimo]
#15---------------------------------------------------------------------------------------------------
def birthday(s, d, m):
    if not s or m>len(s) or m==0 or d==0:
        return 0
        
    if len(s)==m:
        if sum(s)==d:
            return 1
        else:
            return 0
            
    segmentos=[]
    for i in range(len(s)-m+1):
        segmentos.append(s[i:i+m])
        print(s[i:i+m])
    
    sol=0
    for i in segmentos:
        if sum(i)==d:
            sol+=1          
    print(segmentos)
    return sol
#16---------------------------------------------------------------------------------------------------
def divisibleSumPairs(n, k, ar):
    if n==2:
        if sum(ar)%k ==0:
            return 1
        else:
            return 0
    
    sol=0
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            suma=ar[i]+ar[j]
            if suma%k==0:
                sol+=1
    return sol
#17---------------------------------------------------------------------------------------------------
def migratoryBirds(arr):
    counts = [0] * 5
    for bird_type in arr:
        counts[bird_type - 1] += 1
    
    return counts.index(max(counts)) + 1
#18---------------------------------------------------------------------------------------------------
def sockMerchant(n, ar):
    dicci=dict(zip(ar, map(lambda x: ar.count(x), ar)))
    sol=0
    for i in list(dicci.values()):
        sol+=i//2
    return sol
#19---------------------------------------------------------------------------------------------------
def pageCount(n, p):
    if n% 2 !=0:
        n-=1
    res=n//2
    if p<=res:
        return p//2
    else:
        if p% 2 ==0:
            return int(round((n-p)/2, 0))
        else:
            return int(round((n-p)/2+0.5, 0))
#20---------------------------------------------------------------------------------------------------
#21---------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------
#22---------------------------------------------------------------------------------------------------
#23---------------------------------------------------------------------------------------------------
#24---------------------------------------------------------------------------------------------------


#25---------------------------------------------------------------------------------------------------
#26---------------------------------------------------------------------------------------------------
