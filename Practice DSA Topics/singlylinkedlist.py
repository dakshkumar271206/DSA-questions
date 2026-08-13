# class node:
#     def __init__(self,info,next = None):
#         self.data = info
#         self.next = next
# class singlylinkedlist:
#     def __init__(self, head = None):
#         self.head = head
#     # insertion at end
#     def at_end(self, val):
#         tem = node(val)
#         if self.head != None:
#             t1 = self.head
#             while t1.next != None:
#                 t1 = t1.next
#             t1.next = tem
#         else:
#             self.head = tem
#     # insertion at beginning
#     def at_beg(self,val):
#         tem = node(val)
#         tem.next = self.head
#         self.head = tem
#     # insertion in middle
#     def at_mid(self,val,x):
#         tem = node(val)
#         t1 = self.head
#         while t1.next != None:
#             if t1.next == x:
#                 tem.next = t1.next
#                 t1.next = tem
#             else:
#                 t1 = t1.next
#     # deletion
#     def delete(self, val):
#         t1 = self.head
#         pre = t1
#         if t1.data == val:
#             self.head = t1.next
#         while t1.data == val:
#             if t1.data == val:
#                 pre.next = t1.next
#                 break
#             else:
#                 pre = t1
#                 t1 = t1.next
#         if t1.data == val:
#             pre.next = None
#     def Print(self):
#         if self.head is None: # Added check for empty list
#             print("Linked list is empty.")
#             return
#         t1 = self.head
#         while t1.next is not None:
#             print(t1.data, end=" <--> ")
#             t1 = t1.next
#         print(t1.data)
# obj = singlylinkedlist()
# obj.at_end(10)
# obj.at_end(20)
# obj.at_end(30)
# obj.at_beg(0)
# obj.at_mid(5,10)
# obj.delete(5)
# obj.Print()