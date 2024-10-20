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
def countingValleys(steps, path):
    height=0
    situacion_anterior="Nivel del mar"
    sol=0
    for i in path:
        if i =="U":
            height+=1
        elif i=="D":
            height-=1
        if height>0:
            situacion_anterior="Encima nivel del mar"
            continue
        elif height ==0 and situacion_anterior=="Debajo nivel del mar":
            sol+=1
        elif height<0:
            situacion_anterior="Debajo nivel del mar"
    return sol
#21---------------------------------------------------------------------------------------------------
def getMoneySpent(keyboards, drives, b):
    sol=-1
    for i in keyboards:
        budget=b-i
        if budget<=0:
            continue
        for j in drives:
            budget2=budget - j
            if budget2>=0:
                if j+i>sol:
                    sol=j+i
            print(f"Nuestros valores son {i}, {j}, pero actualemnete llevamos {sol}, con un budget de {budget}")
    return sol
#22---------------------------------------------------------------------------------------------------
def matchingStrings(strings, queries):
    result=[]
    for i in queries:
        sol=0
        for j in strings:
            if i==j:
                sol+=1
        print(sol)
        result.append(sol)
    return result
#23---------------------------------------------------------------------------------------------------
def lonelyinteger(a):
    for i in a:
        if a.count(i)==1:
            return i
#24---------------------------------------------------------------------------------------------------
def flippingBits(n):
    binario=bin(n)[2:]
    longitud=len(binario)
    binario2=""
    for i in range(len(binario)):
        if binario[i]=="1":
            binario2+="0"
        elif binario[i]=="0":
            binario2+="1"
    binario2="1"*(32-longitud)+binario2
    decimal=int(binario2, 2)
    return decimal
#25---------------------------------------------------------------------------------------------------
def pangrams(s):
    s=s.lower()
    s=s.replace(" ", "")
    letras=[chr(i) for i in range(97, 123)]
    diccci={}
    for i in letras:
        diccci[i]=0
    for i in s:
        diccci[i]+=1
    if min(list(diccci.values()))>0:
        print("pangram")
    else:
        print("not pangram")
#26---------------------------------------------------------------------------------------------------
def catAndMouse(x, y, z):
    if x>y:
        x-=y
        z-=y
        y-=y
    elif y>x:
        y-=x
        z-=x
        x-=x
    else:
        print("Mouse C")
    distanciaA=abs(z-x)
    distanciaB=abs(z-y)
    
    if distanciaA>distanciaB:
        print("Cat B")
    elif distanciaA<distanciaB:
        print("Cat A")
    else:
        print("Mouse C")
#27---------------------------------------------------------------------------------------------------
def pickingNumbers(a):
    lista=[0]*(max(a)+1)
    for i in a:
        lista[i]+=1
    posibles_sol=[]
    for i in range(len(lista)-1):
        posibles_sol.append(lista[i]+lista[i+1])
    return max(posibles_sol)
#28---------------------------------------------------------------------------------------------------
def designerPdfViewer(h, word):
    letras=[chr(i) for i in range(97, 123)]
    heights=[]
    for letters in word:
        heights.append(h[ord(letters)-97])
    
    return max(heights)*len(word)
#29---------------------------------------------------------------------------------------------------
def angryProfessor(k, a):
    in_time=0
    for i in a:
        if i<=0:
            in_time+=1

    if in_time>=k:
        return "NO"
    else:
        return "YES"
#30---------------------------------------------------------------------------------------------------
#31---------------------------------------------------------------------------------------------------
#32---------------------------------------------------------------------------------------------------
#33---------------------------------------------------------------------------------------------------
#34---------------------------------------------------------------------------------------------------
#35---------------------------------------------------------------------------------------------------
#36---------------------------------------------------------------------------------------------------
#37---------------------------------------------------------------------------------------------------
#38---------------------------------------------------------------------------------------------------
#39---------------------------------------------------------------------------------------------------
#40---------------------------------------------------------------------------------------------------
#41---------------------------------------------------------------------------------------------------
#42---------------------------------------------------------------------------------------------------
#43---------------------------------------------------------------------------------------------------
#44---------------------------------------------------------------------------------------------------
#45---------------------------------------------------------------------------------------------------
#45---------------------------------------------------------------------------------------------------
#46---------------------------------------------------------------------------------------------------
#47---------------------------------------------------------------------------------------------------
#48---------------------------------------------------------------------------------------------------
#49---------------------------------------------------------------------------------------------------
#5---------------------------------------------------------------------------------------------------
