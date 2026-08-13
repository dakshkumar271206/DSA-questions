# class node:
#     def __init__(self, value=None):
#         self.data = value
#         self.next = None
#         self.pre = None
# class doublyLinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert at the end
#     def at_end(self, value):
#         temp = node(value)
#         if self.head is None:
#             self.head = temp
#             return
#         t = self.head
#         while t.next is not None:
#             t = t.next
#         t.next = temp
#         temp.pre = t
#
#     # Insert at beginning
#     def at_beg(self, value):
#         temp = node(value)
#         if self.head is None:
#             self.head = temp
#             return
#         temp.next = self.head
#         self.head.pre = temp
#         self.head = temp
#     # Insert at mid
#     def at_mid(self, value, x):
#         if self.head is None:
#             print("List is empty. Cannot insert at mid.")
#             return
#         t = self.head
#         while t is not None:
#             if t.data == x:
#                 break
#             t = t.next
#         if t is None:
#             print(f"Element {x} not found in the list.")
#             return
#         temp = node(value)
#         temp.next = t.next
#         if t.next is not None:
#             t.next.pre = temp
#         t.next = temp
#         temp.pre = t
#     # Deletion
#     def Del(self, value):
#         if self.head is None:
#             print("Linked list is empty.")
#             return
#         t = self.head
#         # Case 1: Deleting the head node
#         if t.data == value:
#             self.head = t.next  # Changed '==' to '='
#             if self.head is not None: # If list had more than 1 element
#                 self.head.pre = None
#             return
#         # Case 2: Deleting a node in the middle or end
#         while t.next is not None:
#             if t.data == value:
#                 t.pre.next = t.next
#                 t.next.pre = t.pre
#                 return
#             t = t.next  # ADDED: t must advance, otherwise infinite loop!
#         # Case 3: Deleting the very last node
#         if t.data == value:
#             t.pre.next = None
#     def Print(self):
#         if self.head is None: # Added check for empty list
#             print("Linked list is empty.")
#             return
#         t1 = self.head
#         while t1.next is not None:
#             print(t1.data, end=" <--> ")
#             t1 = t1.next
#         print(t1.data)
# obj = doublyLinkedList()
# obj.at_end(10)
# obj.at_end(20)
# obj.at_end(30)
# obj.at_beg(0)
# obj.at_mid(5,10)
# obj.Del(5)
# obj.Print()