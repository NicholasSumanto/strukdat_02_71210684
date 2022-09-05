import timeit

#iteratif
def fib_iter(n):                                                                                                 
    fibs = [0, 1, 1]                                                                                           
    for f in range(2, n):                                                                                      
        fibs.append(fibs[-1] + fibs[-2])                                                                         
    return fibs[n]

#rekursif
def fib_rekur(n):
    if n < 2:
        return n
    return fib_rekur(n-2) + fib_rekur(n-1)


#WAKTU
for i in range (1,101):
    start1 = timeit.default_timer()
    hasil1 = fib_iter(i)
    end1 = timeit.default_timer()
    start2 = timeit.default_timer()
    hasil2 = fib_rekur(i)
    end2 = timeit.default_timer()
    print ("Fibonanci ke:",i,"\n""ITERATIF =",end1-start1,"\n""REKURSIF =",end2-start2)






