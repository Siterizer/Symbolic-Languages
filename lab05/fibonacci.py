def iter(n):
    x,y=1,1
    for i in range(n-1):
        y = x + y
        x = y - x
    return y
def rek(n):
    if n == 1 or n == 0:
        return 1
    return rek(n-1) + rek(n - 2)
