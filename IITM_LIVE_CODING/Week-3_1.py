class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.l = []
    def isEmpty(self):
        return self.head == None
     
    # Method to add an item to the queue
    def Enqueue(self, item):
        temp = Node(item)
        self.l.append(item)
        if self.head == None:
            self.head = self.last = temp
            return
        self.last.next = temp
        self.last = temp
 
    # Method to remove an item from queue
    def Dequeue(self):
         
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.next
 
        if(self.head == None):
            self.last = None
        z = self.l[0]
        self.l = self.l[1:]
        return z
