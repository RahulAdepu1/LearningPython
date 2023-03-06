# Accessing/Traversing the list
shopList = ['Milk', 'Cheese', 'Butter']
print(shopList[1])
print('Milk' in shopList)
print(shopList[-1])

print("---------------")
for i in shopList:
    print(i)

print("---------------")
for i in range(len(shopList)):
    shopList[i] = shopList[i]+"+"
    print(shopList[i])
print("---------------")


# Update/Insert in List
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] =33
print(myList)

print("---------------")
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
print("Insert")
myList.insert(0, 11)
print(myList)
print("---------------")
print("Append")
myList.append(55)
print(myList)
print("---------------")
print("Extend")
myList1 = [11, 12, 13]
myList.extend(myList1)
print(myList)
print("---------------")

# Slice/Delete in List
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList[0:2])
print(myList[:2])
print(myList[1:])
print(myList[:])

myList[0:2] = [11, 12]
print(myList)
print("---------------")
print("Pop")
myList.pop(1)  # pop(index)
print(myList)
print("---------------")
print("Delete")
del myList[3]
print(myList)
del myList[:2]
print(myList)
print("---------------")
print("Remove")
myList.remove(4)
print(myList)
print("---------------")

# Searching in list
print("Search")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if 2 in myList:
    print(myList.index(2))
else:
    print("Value does not exist")

print("---------------")
print("Linear Search")
def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'Value not found'

print(searchInList(myList, 4))
print("---------------")

# Operations/Functions in List
print("'+' Operator")
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)
print("---------------")
print("'*' Operator")
a = [0]
a = a * 4
print(a)
a = [0,1]
a = a * 4
print(a)

print("---------------")
print("Length")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(myList))

print("---------------")
print("min()")
print(min(myList))

print("---------------")
print("max()")
print(max(myList))

print("---------------")
print("sum()")
print(sum(myList))

print("---------------")
print("Average")
print(sum(myList)/len(myList))

print("---------------")
# String in list

a = 'spam-spam-spam'
b = a.split('-')
print(b)
c = '-'
print(c.join(b))
print('-'.join(b))
print("---------------")
