def flatten(arr):
    tempArray = []
    for item in arr:
        if type(item) is list:
            tempArray.extend(flatten(item))
        else:
            tempArray.append(item)
    return tempArray

print(flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5])
print(flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5])
print(flatten([[1], [2], [3]]) # [1, 2, 3])
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3])