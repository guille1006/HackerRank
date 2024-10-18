#1---------------------------------------------------------------------------------------------------
def formingMagicSquare(s):
    # Poner el 5 de el centro:
    sol=abs(5-s[1][1])
    s[1][1]=5
    
    # Creamos el cuadrado
    square=[]
    for i in range(3):
        square.append(s[0][i])
    square.append(s[1][2])
    for i in range(2, -1, -1):
        square.append(s[2][i])
    square.append(s[1][0])
    
    # Primer cuadrado de referencia
    cuadrado1=[8, 3, 4, 9, 2, 7, 6, 1]
    # Segundo cuadrado de referencia
    cuadrado2=[cuadrado1[0]]+cuadrado1[:0:-1]
    
    posibles_sol=[]
    
    for _ in range(4):
        posible_sol=0
        for j, i in zip(square, cuadrado1):
            posible_sol+=abs(j-i)
        posibles_sol.append(posible_sol)
        
        posible_sol=0
        for j, i in zip(square, cuadrado2):
            posible_sol+=abs(j-i)
        posibles_sol.append(posible_sol)
    
        cuadrado1=cuadrado1[2:]+cuadrado1[:2]
        cuadrado2=cuadrado2[2:]+cuadrado2[:2]
    
    return min(posibles_sol)+sol
def valores(s):
    valores=[0]*9
    for i in range(3):
        for j in range(3):
            valores[s[i][j]-1]+=1
    sobran=[]
    faltan=[]
    for i in range(9):
        if valores[i]>1:
            sobran+=[i+1]*(valores[i]-1)
        if valores[i]==0:
            faltan+=[i+1]
        
    return f"faltan {faltan}, sobran{sobran}"        
def sumas(s):
    sumas=[]
    diagonal_positiva=0
    diagonal_negativa=0
    n=len(s)
    for i in s:
        sumas.append(sum(i))
    for i in range(n):
        diagonal_positiva+=s[i][i]
        diagonal_negativa+=s[i][-(i+1)]
    sumas.append(diagonal_positiva)
    sumas.append(diagonal_negativa)
    columna=0
    for i in range(n):
        for j in range(n):
            columna+=s[j][i]
        sumas.append(columna)
        columna=0
    print(sumas)
    return sumas
#2---------------------------------------------------------------------------------------------------
def climbingLeaderboard(ranked, player):
    positions=[]
    sol=[]
    for i in ranked:
        if i in positions:
            continue
        else:
            positions.append(i)
    positions.append(0)

    for i in player:
        try:
            index=positions.index(i)
        except:
            index= searchInsert(positions,i)
            positions=positions[:index]+[i]+positions[index:]
            sol.append(index+1)
        else:
            sol.append(1+positions.index(i))
            
    return sol  
def searchInsert(nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
def climbingLeaderboard_por_un_random(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    rankFinal: list = []
    #print(ranked)
    
    for ply in player:
        for rankPos, rankScore in enumerate(ranked, 1):
            if ply >= rankScore:
                #print(ply, rankPos, rankScore)
                rankFinal.append(rankPos)
                break
            if rankPos == len(ranked):
                #print(ply, rankPos+1)
                rankFinal.append(rankPos+1)
    
    return rankFinal
    
#3---------------------------------------------------------------------------------------------------
#4---------------------------------------------------------------------------------------------------
#5---------------------------------------------------------------------------------------------------
#6---------------------------------------------------------------------------------------------------
#7---------------------------------------------------------------------------------------------------
#8---------------------------------------------------------------------------------------------------
#9---------------------------------------------------------------------------------------------------
#10---------------------------------------------------------------------------------------------------
#11---------------------------------------------------------------------------------------------------
#12---------------------------------------------------------------------------------------------------
#13---------------------------------------------------------------------------------------------------
#14---------------------------------------------------------------------------------------------------
#15---------------------------------------------------------------------------------------------------
#16---------------------------------------------------------------------------------------------------
#17---------------------------------------------------------------------------------------------------
#18---------------------------------------------------------------------------------------------------
#19---------------------------------------------------------------------------------------------------
#20---------------------------------------------------------------------------------------------------
#21---------------------------------------------------------------------------------------------------
#22---------------------------------------------------------------------------------------------------