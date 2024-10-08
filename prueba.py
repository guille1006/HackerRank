def getTotalX(a, b):
    avieja=a
    #Lo primero que hago es ver si los del grupo a son factores de los del grupo b
    for i in a:
        for j in b:
            if j%i!=0:
                return sol
            
    #Ahora lo que hago es quitar del grupo a los valores que ya son factores de un numero mayor
    for i in a[::-1]:
        for j in a[:]:
            print(f"todo nuestro a es {a}")
            print(f"cogemos como valor j:{j}")
            if i==j:
                print(f"tanto {i} como {j}")
                pass
            elif i%j==0:
                print(f"nuestro valor {j}, es {i}")
                print(f"vamos a borrar{a.index(j)}")
                a.pop(a.index(j))
        print(a)
    print(a)
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

a=[3,9,6]
b=[36,72]
getTotalX(a,b)