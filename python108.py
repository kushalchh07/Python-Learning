# Queues and Stack in python
#using list

from queue import Queue
from queue import LifoQueue

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
q.put(7)
q.put(8)
q.put(9)
q.put(10)

while not q.empty():
    print(q.get())
    
 #using deque
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
q.append(8)
q.append(9)
q.append(10)

while q:
    print(q.popleft())
    
#stack

s = LifoQueue() # last in first out is lifo which is stack

s.put(1)
s.put(2)
s.put(3)
s.put(4)
s.put(5)
s.put(6)
s.put(7)
s.put(8)
s.put(9)
s.put(10)

while not s.empty():
    print(s.get())