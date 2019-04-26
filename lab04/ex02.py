def function(x, y):
    return y, x+y
def fib(n):
    k=(0, 1)
    for i in range(n):
        k = function(*k)
    return k[0]

print(fib(14))
