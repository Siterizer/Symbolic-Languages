def function(list1, list2):
    return [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]


print(function([1, 2, 3, 4, 5], [7, 6, 5, 4, 6, 8, 8, 6, 7, 8]))
