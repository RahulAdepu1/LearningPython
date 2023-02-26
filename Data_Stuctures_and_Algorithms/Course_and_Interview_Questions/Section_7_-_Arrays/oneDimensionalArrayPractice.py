# Practice Questions
from array import *

# 1.Create an array and traverse
print("Step 1")
array1 = array('i',[1,2,3,4,5])
for i in array1:
    print(i)
print("---------------------------")
# 2.Access individual elements through indexes
print("Step 2")
print(array1[0])

print("---------------------------")
# 3.Append any value to the array using append() method
print("Step 3")
array1.append(6)
print(array1)

print("---------------------------")
# 4.Inset value in an array using insert() method
print("Step 4")
array1.insert(3,11)
print(array1)

print("---------------------------")
# 5.Extend python array using extend() method
print("Step 5")
array2 = array('i',[10,11,12])
array1.extend(array2)
print(array1)

print("---------------------------")
# 6.Add items from list into array using fromlist() method
print("Step 6")
tempList = [20,21,22]
array1.fromlist(tempList)
print(array1)

print("---------------------------")
# 7.Remove any array element using remove() method
print("Step 7")
array1.remove(11)
print(array1)

print("---------------------------")
# 8.Remove last array element using pop() method
print("Step 8")
array1.pop()
print(array1)

print("---------------------------")
# 9.Fetch any element through its index using index() method
print("Step 9")
print(array1.index(21))

print("---------------------------")
# 10.Reverse a python array using reverse() method
print("Step 10")
array1.reverse()
print(array1)

print("---------------------------")
# 11.Get array buffer information through buffer_info() method
print("Step 11")
print(array1.buffer_info())

print("---------------------------")
# 12.Check for number of occurrence of an element using count() method
print("Step 12")
array1.append(11)
print(array1.count(11))

print("---------------------------")
# 13.Convert array to string using tostring() method
print("Step 13")
# strTemp = array1.tostring()
# print(strTemp)

print("---------------------------")
# 14.Convert array to a python list with same elements using tolist() method
print("Step 14")
print(array1.tolist())

print("---------------------------")
# 15.Append a string to char array using fromstring() method
print("Step 15")

print("---------------------------")
# 16.Slice elements from an array
print("Step 16")
print(array1[0:3])

