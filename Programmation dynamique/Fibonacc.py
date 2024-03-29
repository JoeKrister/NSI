def fibo(n : int) -> int :
    if n == 0 :
        return  0
    elif n == 1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

# import time
# for n in range(40) :
#     start = time.perf_counter()
#     print(f"fibo({n}) = {fibo(n)}", end="")
#     end = time.perf_counter()
#     print(f" Temps : {end - start}")

def fiboAsc(n : int) -> int :
    F = [0]*(n+1)
    F[1] = 1
    for i in range(2,n+1) :
        F[i] = F[i-1] + F[i-2]
    return F[n]
