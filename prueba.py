def divisibleSumPairs(n, k, ar):
    if n==2:
        if sum(ar)%k ==0:
            return 1
        else:
            return 0

print(divisibleSumPairs(2,3,[1,2]))