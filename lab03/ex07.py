def function(list):
    for i, j in enumerate(list):
        if i % 3 == 0 or j < 0:
            del list[i]
    return list


print(function([5, 6, 8, 54, 67, 8, -56, -56, -56, 34, -6, 1, 2, 3]))
