def function(list):
    list.sort()
    return list[:3] + list[len(list) - 3:]


print(function([1, 76, 4, 85, 3, 67, 885, 457, 8, 6, 4, 6, 4, 7, 975]))
