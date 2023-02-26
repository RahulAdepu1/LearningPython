import numpy as np

twoDimArray = np.array([[11, 15, 10, 6],
                        [10, 14, 11, 5],
                        [12, 17, 12, 8],
                        [15, 18, 14, 9]])

print(twoDimArray)
print("--------------------")
# inset a value in two-dimensional array a[i][j]
# adding column
newTwoDimArray = np.insert(twoDimArray, 0, [[1, 2, 3, 4]], axis=1)
print(newTwoDimArray)
print("--------------------")

# adding row
newTwoDimArray = np.insert(twoDimArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDimArray)
print("--------------------")

# append column at the end of two-dimensional array
newTwoDimArray = np.append(twoDimArray, [[1], [2], [3], [4]], axis=1)
print(newTwoDimArray)
print("--------------------")

# append row at the end of two-dimensional array
newTwoDimArray = np.append(twoDimArray, [[1, 2, 3, 4]], axis=0)
print(newTwoDimArray)
print("--------------------")

# accessing an element of a two-dimensional array
def accessElement(array, rowIndex, colIndex):
    if rowIndex >=len(array) and colIndex >= len(array[0]):
        print("Error")
    else:
        print(array[rowIndex][colIndex])

accessElement(twoDimArray, 2, 3)
print("--------------------")

# Traversing of two_dimensional array
for i in range(len(twoDimArray)):
    for j in range(len(twoDimArray[0])):
        print(twoDimArray[i][j])

print("--------------------")

# Search for a value in a two-dimensional array
def searchTwoDimArray(array, value):
    for i in range(len(twoDimArray)):
        for j in range(len(twoDimArray[0])):
            if array[i][j] == value:
                return 'The value is at row->'+str(i)+' col->'+str(j)
    return 'The element not found'

print(searchTwoDimArray(twoDimArray, 8))
print("--------------------")

deleteTwoDimArray = np.delete(twoDimArray, 0, axis=1)
print(deleteTwoDimArray)
