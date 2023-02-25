def capitalizeWords(arr):
    tempArray = []
    if len(arr)==0:
        return tempArray
    tempArray.append(arr[0].upper())
    return tempArray + capitalizeWords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words))