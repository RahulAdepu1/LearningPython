# Creation
class Node:
    def __init__(self, value=None):
        self.value = value
        print("Initialising Node self.value ", self.value)
        self.next = None
        print("Initialising Node self.next ", self.next)

class SLL:
    def __init__(self):
        self.head = None
        print("Initialising List self.head ", self.head)
        self.tail = None
        print("Initialising List self.tail ", self.tail)

    def __iter__(self):
        node = self.head
        print("Iterating node val = ", node," and self.value = ", self.head)
        while node:
            yield node
            node = node.next
            print("Iterating node.next ", node)

    # Insertion
    def insertSLL(self, value, location):
        print("--------Inside Insert--------")
        print("Value =", value)
        print("Location =", location)
        newNode = Node(value)
        print("newNode =", newNode)
        print("Self.head =", self.head)
        if self.head is None:
            print("--Making new list--")
            self.head = newNode
            print("Self.head val =", self.head)
            self.tail = newNode
            print("Self.tail val =", self.tail)
        else:
            if location == 0:
                print("--------------------------------")
                print("--Adding New Node at the start--")
                print("--------------------------------")
                newNode.next = self.head
                print("NewNode.next =", newNode.next)
                self.head = newNode
                print("self.head =", self.head)
            elif location == -1:
                print("------------------------------")
                print("--Adding New Node at the End--")
                print("------------------------------")
                newNode.next = None
                self.tail.next = newNode
                print("self.tail.next =", self.tail.next)
                self.tail = newNode
                print("self.tail =", self.tail)
            else:
                print("---------------------------------")
                print("--Adding New Node in the middle--")
                print("---------------------------------")
                tempNode = self.head
                print("tempNode =", tempNode)
                index = 0
                print("index =", index, " and (location - 1) =", location-1)
                while index < location - 1:
                    tempNode = tempNode.next
                    print("tempNode =", tempNode)
                    index += 1
                    print("index =", index, " and (location - 1) =", location-1)
                nextNode = tempNode.next
                print("nextNode =", nextNode)
                tempNode.next = newNode
                print("tempNode.next =", tempNode.next)
                newNode.next = nextNode
                print("newNode.next =", newNode.next)
                print("tempNode =", tempNode)
                print("self.tail =", self.tail)
                if tempNode == self.tail:
                    self.tail = newNode
                    print("self.tail =", self.tail)

    # Traversal
    def traverseSLL(self):
        if self.head is None:
            print("Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Searching
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "Singly Linked List does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Value does not exist"

    # Deletion
    def deleteSLL(self, location):
        if self.head is None:
            return "Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Entire Deletion
    def deleteEntireSLL(self, location):
        if self.head is None:
            return "Singly Linked List does not exist"
        else:
            self.head = None
            self.tail = None



# -----Creation of Singly Linked List-----
# singlyLL = SLL()
# node1 = Node(1)
# node2 = Node(2)
#
# singlyLL.head = node1
# singlyLL.head.next = node2
# singlyLL.tail = node2

# -----Insertion of Singly Linked List-----
# singlyLL = SLL()
# singlyLL.insertSLL(1, -1)
#
# # To insert a value at the Start
# singlyLL.insertSLL(0, 0)
# # To insert a value at the End
# singlyLL.insertSLL(3, -1)
# # To insert a value after the 3RD ELEMENT
# singlyLL.insertSLL(2, 2)
#
# print([node.value for node in singlyLL])

# -----Searching-----
# singlyLL = SLL()
# singlyLL.insertSLL(1, -1)
# singlyLL.insertSLL(2, -1)
# singlyLL.insertSLL(3, -1)
# singlyLL.insertSLL(4, -1)
# singlyLL.insertSLL(0, 0)
# singlyLL.insertSLL(0, 4)
#
# print([singlyLL.searchSLL(5)])

# -----Deletion-----
# singlyLL = SLL()
# singlyLL.insertSLL(1, -1)
# singlyLL.insertSLL(2, -1)
# singlyLL.insertSLL(3, -1)
# singlyLL.insertSLL(4, -1)
# singlyLL.insertSLL(0, 0)
# singlyLL.insertSLL(0, 4)
#
# print([node.value for node in singlyLL])
# singlyLL.deleteSLL(2)
# print([node.value for node in singlyLL])