def function(list ,x):
    i=0
    while i < len(list):
        if i % x == 0:
            list.insert(i,0)
        i+=1
    return list





print(function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))