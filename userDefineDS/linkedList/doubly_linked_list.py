

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
        print()
        if self.head is None:
            print("Linked list is empty !")
        else:
            n = self.head  # take the first node and assign to n variable # head is a starting point of the linklist
            while n.nref is not None:  #  it will reach to the last node and the conditionwillbe False and the loop will stop
                n = n.nref
            while n is not None:  # means is not empty the condition will stop when the last node will point to none
                print(n.data, "--->", end="")
                n = n.pref

    # Insert node when the linkedlist is empty
    def insert_empty(self, data):
        if self.head is None:  # if the head is none we have to insert the new node
            new_node = Node(data)
            # after creating the new node point the head to the new node
            self.head = new_node
        else:
            print("linked list is not empty ! ")

    # Insert element at the beginning of link list
    def add_begin(self, data):
        new_node = Node(data)  # create new node
        if self.head is None: # check if the node is empty if it is create the new node
            self.head = new_node
        else:
            new_node.nref = self.head  # we assign the head to new node next reference
            self.head.pref = new_node
            self.head = new_node

    # Insert element at the end of the link list
    def add_end(self, data):
        new_node = Node(data)  # create new node
        if self.head is None:  # before adding element at the end of the link list you must first check if the llist is empty or not is it empty create the new node and point the head to the new node
            self.head = new_node
        else:
            n = self.head  # if its not empty we assign the first node to n
            while n.nref is not None:  # n.nref is to travel to the last next reference node if its become null the condition fails and the loop will stop
                n = n.nref  # after traversing the n become null come out of the loop
            n.nref = new_node
            new_node.pref = n


ddl1 = doublyLL()
ddl1.insert_empty(10)
ddl1.add_begin(20)
ddl1.add_end(100)
ddl1.printLL()
ddl1.printLL_reverse()

