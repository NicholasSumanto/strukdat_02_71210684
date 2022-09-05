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


#time iter
print("ITERATIF")

for i in range (1,101):
    start = timeit.default_timer()
    hasil = fib_iter(i)
    end = timeit.default_timer()
    print ("fibonanci ke:",i,"=",hasil,"waktu:",end-start)


#time rekur
print()
print("REKURSIF")
for i in range (1,101):
    start = timeit.default_timer()
    hasil = fib_rekur(i)
    end = timeit.default_timer()
    print ("fibonanci ke:",i,"=",hasil,"waktu:",end-start)



