def function(x):
    return [[j % 2 for j in range(i % 2, x + i % 2)] for i in range(1, x + 1)]



print(function(3))