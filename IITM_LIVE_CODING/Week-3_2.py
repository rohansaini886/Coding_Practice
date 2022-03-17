class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
      
    def insert_end(self,data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:            
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
    
    def insert_at_pos(self, newElement, position):     
        newnode = Node(newElement)
        if(position < 1):
          print("\nposition should be >= 1.")
        elif (position == 1):
          newnode.next = self.head
          self.head.prev = newnode
          self.head = newnode
        else:    
          temp = self.head
          for i in range(1, position-1):
            if(temp != None):
              temp = temp.next   
          if(temp != None):
            newnode.next = temp.next
            newnode.prev = temp
            temp.next = newnode  
            if (newnode.next != None):
              newnode.next.prev = newnode
          else:
            print("\nThe previous node is null.")
