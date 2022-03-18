class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, key):
        self.items.insert(0,key)
    def dequeue(self):
        return self.items.pop()
            
class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0
        self.list = []
    def push(self, data):
        self.list.append(data)
        self.size += 1
    def pop(self):
        x = self.list[-1]
        self.list.pop(-1)
        self.size -= 1
        return(x)
    def top(self):
        return self.list[self.size-1]
    def isempty(self):
        if self.size == 0:
            return('True')
        else:
            return('False')
        
inp = eval(input())
dl = int(input())
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())
