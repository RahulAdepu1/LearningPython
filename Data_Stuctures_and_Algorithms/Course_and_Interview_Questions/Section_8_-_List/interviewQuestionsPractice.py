print("Q1 - Find the missing number")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def findMissing(list):
    for i in range(len(list) - 1):
        if i + 1 != list[i]:
            print(i + 1)
            break

findMissing(mylist)
print("--------------------------")
print("Q2 - Find Pairs /Two Sum")


print("--------------------------")
print("Q3 - Find a number in an Array")


