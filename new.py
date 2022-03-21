def printfibonaccinumbewres(n) :
    a = 0
    b = 1
    if (n<1):
        return
    print(a, end=" " )
    for x in range (1 , n):
        print(b, end=" ")
        c = a + b
        a = b
        b = c

printfibonaccinumbewres(10)
