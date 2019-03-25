def FibBinet(n):
    raiz5 = 5 ** 0.5
    fib = (((1+raiz5)/2)**n - ((1-raiz5)/2)**n)/raiz5
    return fib

entrada = float(input())

print("%.1f"%(FibBinet(entrada)))
