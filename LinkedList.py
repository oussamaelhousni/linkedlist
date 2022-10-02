from ast import Not
from pickle import FALSE


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    # better representation of a linkedlist
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # make a linked traversable using for loop
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    # add new node to the linked list
    def addNode(self,node):
        if self.head is None:
            self.head = node
            return
        for currentNode in self:
            pass
        # the currentNode hold inside it the last node
        currentNode.next = node
    
    # add a node at the beginning of the likedlist
    def addFirst(self,node):
        node.next = self.head
        self.head = node

    def addLast(self,newNode):
        if self.head is None:
            self.addFirst(newNode)
            return
        for node in self:
            pass
        node.next = newNode

    # add a node after a specific node in the list
    def addAfter(self,value,node):
        if self.head is None:
            raise Exception("The list is empty")
        
        for currentNode in self:
            if currentNode.data == value:
                node.next = currentNode.next
                currentNode.next = node
                return
        raise Exception("Node with data '%s' not found" % str(value))

    # add a node before a specific node in the list
    def addBefore(self,value,newNode):
        if self.head is None:
            raise Exception("The list is empty")

        if self.head.data == value:
            newNode.next = self.head
            self.head = newNode
            return
        
        previous = None
        for node in self:
            if node.data == value:
                previous.next = newNode
                newNode.next = node
                break
            previous = node
        raise Exception("Node with data '%s' not found" % str(value))

    # remove a node from linkedlist
    def remove(self,value):
        if self.head is None:
            raise Exception("The list is empty")
        
        if self.head.data == value:
            self.head = self.head.next
            return

        previous = None
        for node in self:
            if node.data == value:
                previous.next = node.next
                return
            previous = node
        raise Exception("Node with data '%s' not found" % str(value))

    # delete a node from the linkedlist

    # the length of the linkedlist
    def length(self):
        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.next
        return count

    # insert a node in a specific  position
    def insertAtPos(self,pos,newNode):
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return

        if pos > self.length() or pos < 0:
            raise Exception("You've entered invalid position")

        if pos == self.length():
            self.addLast(newNode)
            return
        
        node = self.head
        count=0
        while count < pos-1:
            node  = node.next
            count = count + 1
        newNode.next = node.next
        node.next = newNode

    # F'ind nth node from the end of a Linked List.
    def kElemFromTheEnd(self,k):
        if k >= self.length() or k < 0:
            raise Exception("Invalid position")
        
        if self.head is None:
            raise Exception("The list is empty")
        
        node = self.head
        count = 0
        while node is not None and count < k:
            count = count + 1
            node = node.next

        if node is None:
            return None

        secondNode = self.head
        while node is not None:
            secondNode = secondNode.next
            node = node.next
        return secondNode

    # Check whether the given linked list is either NULL-terminated or ends in a cycle 
    def hasCycleHashTable(self):
        if self.head is None:
            return False
        dict = {}
        node = self.head
        while node is not None:
            if node in dict.keys():
                return False
            if node.next in dict.values():
                return True
            dict[node]=node.next
            node = node.next
        return False

    # check a linked list has a cycle
    def hasCycleFloyd(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast is not None:
            fast = fast.next
            if slow == fast:
                return True
            if fast is None:
                return False
            fast = fast.next 
            if slow == fast:
                return True
            slow = slow.next
    
    # find the start of the cycle
    def startOfCycle(self):
        # check if the lost contain a cycle        
        if not self.hasCycleFloyd():
            return None
        
        slow = self.head.next
        fast = slow.next
        # i didn't check for None because list contains already cycle
        while fast != slow:
            slow = slow.next
            fast = fast.next.next
        slow = self.head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow

    # find the length of the cycle
    def cycleLength(self):
        if not self.hasCycleFloyd():
            raise Exception("This linkedlist doesn't contain a cycle")
        slow = self.head
        fast = self.head.next
        while fast != slow:
            slow = slow.next
            fast = fast.next.next
        count = 1
        slow = slow.next
        while slow != fast:
            count = count + 1
            slow = slow.next
        return count

    # insert in a sorted list
    def insertSorted(self,value):
        newNode = Node(value)
        if self.head is None:
            self.addFirst(newNode)
            return

        if self.head.data > value:
            self.addFirst(newNode)
            return
        node = self.head
        while node.next is not None and node.next.data < value:
            node = node.next
        
        if node.next is None:
            node.next = newNode
            return
        
        newNode.next = node.next
        node.next = newNode

    # inverse a linkedlist
    def inverse(self):
        if self.head is None:
            return self.head
        
        next = None
        previuos = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previuos
            previuos = current
            current = next
        self.head = previuos

    # inverse a linkedlist using recursion
    def inverseRecursively(self,node):
        if node is None:
            return
        # get the a linkedlist that starts from the second element
        second = node.next
        if node == self.head:
            node.next = None
        else:
            node.next = self.head
            self.head = node
        self.inverseRecursively(second)
        

            


        
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1 = Node(1)
n2 = Node(2)
list = LinkedList()
list.insertSorted(3)
list.insertSorted(4)
list.insertSorted(5)

list.insertSorted(1)
list.insertSorted(2)

""" n2.next = n3
list.addNode(n2) """
list.inverseRecursively(list.head)
print(list)