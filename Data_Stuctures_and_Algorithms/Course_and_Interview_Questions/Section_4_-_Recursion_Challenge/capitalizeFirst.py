def capitalizeFirst(arr):
    tempArray = []
    if len(arr) == 0:
        return tempArray
    tempArray.append(arr[0].capitalize())
    return tempArray + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car', 'taco', 'banana']))