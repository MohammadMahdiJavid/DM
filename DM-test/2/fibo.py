def fibo(n):
    if n<3:
        return n-1
    else:
        return fibo(n-1)+fibo(n-2)
