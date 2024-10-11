
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
    decimal=int(binario2,2)
    print(decimal)

flippingBits(9)