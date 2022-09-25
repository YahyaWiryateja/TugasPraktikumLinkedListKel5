from lib2to3.pytree import Node
from os import link
from platform import node
from uuid import getnode

class LinkedList:
    def __init__(self):
        self.head = None

    def addDepan(self, data):
        tempNode = Node(data)
        tempNode.setnext(self.head)
        self.head = tempNode
        del tempNode
    
    def addBelakang(self, data):
        start = self.head
        tempNode = Node(data)
        while start.getNextNode():
            start = start.getNextNode()
        start.setnext(tempNode)
        del tempNode
        return True

    def length(self):
        start = self.head
        size = 0
        while start:
            size += 1
            start = start.getNextNode()
        return size

    def Swap(self, x, y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
   
        if prevX != None:
            prevX.next = currY
        else: 
            self.head = currY
     
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def remove(self, item):
        start = self.head
        previous = None
        found = False
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setnext(start.getNextNode())
        return found

    def get(self, index):
        if index>=self.length():
            print ("error")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.getNextNode
            if cur_idx==index: return cur_node.data
            cur_idx+=1
    
    def deleteNode(self, key): #Soal nomor 1
            
            temp = self.head
    
            if (temp is not None):
                if (temp.data == key):
                    self.head = temp.next
                    temp = None
                    return
    
            while(temp is not None):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
    
            if(temp == None):
                return
    
            prev.next = temp.next
    
            temp = None
    
    def removedup(self): #Soal nomor 2
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head
        while (ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            while (ptr2.next  != None):
                if (ptr1.data == ptr2.next .data):
                    dup = ptr2.next
                    ptr2.next  = ptr2.next .next
                else:

                    ptr2 = ptr2.next
            ptr1 = ptr1.next  

    def TailtoFront(self): #Soal nomor 3
        tmp = self.head
        sec_last = None
        while tmp and tmp.next:
            sec_last = tmp
            tmp = tmp.next
        sec_last.next = None
        tmp.next = self.head
        self.head = tmp     
 
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end="")
            start = start.next
            if start:
                print("", end="")
        print()


        

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def updateData(self, data):
        self.data = data

    def setnext(self, node):
        self.next = node

    def getData(self):
        return self.data
    
    def getNode(data):
        newNode = next(data)
        return newNode

    def getNextNode(self):
        return self.next

myList = LinkedList()
myList.addDepan('p')
myList.addDepan('a')
myList.addDepan('s')
myList.addDepan('l')
myList.addDepan('a')
myList.addDepan('a')
myList.display()
myList.removedup() #soal nomor 2
myList.display()
myList.TailtoFront() #soal nomor 3
myList.display()
myList.deleteNode(3) #soal Nomor 1
myList.addBelakang('a')
myList.display()
