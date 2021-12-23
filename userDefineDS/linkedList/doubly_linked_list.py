

class Node:
    # this program the reference will be None or NULL by default
    def __init__(self, data):
        self.data = data
        # both reference must be null initialy
        self.nref = None  # next reference
        self.pref = None  # previous reference


class doublyLL:
    def __init__(self):
        # head = None, mean the doubly linkedList is empty
        self.head = None

    # define the operation for doubly linkedlist , Insertion , deletionand traversal operations
    def printLL(self):
        # let talk here about traversal doublylinkedList we go to doublelinklist and we print each data
        # FORWARD DIRECTION
        if self.head is None:
            print("Linked list is empty !")
        else:
            n = self.head  # take the first node and assign to n variable # head is a starting point of the linklist
            while n is not None:  # means is not empty the condition will stop when the last node will point to none
                print(n.data, "--->", end="")
                n = n.nref # take the reference of the n

    def printLL_reverse(self):
        # REVERSE DIRECTION
        if self.head is None:
            print("Linked list is empty !")
        else:
            n = self.head  # take the first node and assign to n variable # head is a starting point of the linklist
            while n.nref is not None:  #  it will reach to the last node and the conditionwillbe False and the loop will stop
                n = n.nref
            while n is not None:  # means is not empty the condition will stop when the last node will point to none
                print(n.data, "--->", end="")
                n = n.pref

ddl1 = doublyLL()
# ddl1.printLL()
# ddl1.printLL_reverse()

