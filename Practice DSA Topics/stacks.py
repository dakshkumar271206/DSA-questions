# ##stacks
# class stack:
#     def __init__(self):
#         self.s = []
#     ##length of the stack
#     def Len(self):
#         return len(self.s)
#     ##push 
#     def push(self, value):
#         self.s.insert(0, value)
#     ##peek
#     def peek(self):
#         if len(self.s) == 0:
#             raise Exception("stack is empty.")
#         else:
#             return self.s[0]
#     ##pop
#     def pop(self):
#         if len(self.s) == 0:
#             raise Exception("stack is empty.")
#         else:
#             return self.s.pop(0)
# stk = stack()
# stk.push(10)
# stk.push(20)
# stk.push(30)
# print(stk.peek())
# print(stk.pop())
# print(stk.pop())
# print(stk.pop())
## queues and dequeues
# class queue:
#     def __init__(self):
#         self.q = []
#     ## length of queue
#     def Len(self):
#         if len(self.q) == 0:
#             print("Empty queue.")
#         else:    
#             return len(self.q)
#     ## enqueue the element
#     def enqueue(self,value):
#         self.q.append(value)
#     ## dequeue the element
#     def dequeue(self):
#         return self.q.pop(0)
# obj = queue()
# #print(obj.Len())
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# print(obj.dequeue())
# print(obj.dequeue())
#print(obj.dequeue())
# class deque:
#     def __init__(self):
#         self.de = []
#     ## length of deque
#     def Len(self):
#         if len(self.q) == 0:
#             print("Empty queue.")
#         else:
#             return len(self.q)
#     ## enqueue in deque
#     def Endeque(self,value):
#         dire = input("Enter the direction: (rear:'r' or front:'f)")
#         if(dire == 'f'):
#             self.de.insert(0,value)
#         elif(dire == 'r'):
#             self.de.append(value)
#         else:
#             print("invaild input!")
#     ## dequeue in deque
#     def Dedeque(self,value):
#         dire = input("Enter the direction: (rear:'r' or front:'f)")
#         if(dire == 'f'):
#             self.de.pop(0)
#             return value
#         elif(dire == 'r'):
#             self.de.pop()
#             return value
#         else:
#             print("invaild input!")
# obj = deque()
# obj.Endeque(1,'f')
# obj.Endeque(2,'r')
# print(obj.Dedeque(1,))
# print(obj.Dedeque(2,))
# class circular_queue:
#     def __init__(self,size):
#         self.size = size
#         self.cq = [None] * size
#         self.front = self.rear = -1
#     def insert(self,value):
#         if(self.rear + 1) % self.size == self.front:
#             print("queue is full.")
#         elif self.rear == -1 or self.front == -1:
#             self.front = self.rear = 0
#             self.cq[self.rear] = value
#         else:
#             self.rear = (self.rear + 1) % self.size
#             self.cq[self.rear] = value
#     def delete(self):
#         if(self.front == -1 or self.rear == -1):
#             print("empty.")
#         elif self.front == self.rear:
#             print(self.cq[self.front])
#             self.front = self.rear = -1
#         else:
#             print(self.cq[self.front])
#             self.front = (self.front + 1) % self.size
# cq = circular_queue(5)
# cq.insert(10)
# cq.insert(20)
# cq.insert(30)
# cq.insert(40)
# cq.insert(50)
# cq.delete()
# cq.insert(60)
# cq.delete()
# cq.delete()
# cq.delete()
# cq.delete()
# cq.delete()
# cq.delete()