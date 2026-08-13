# # class node:
# #     def __init__(self, val):
# #         self.left = None
# #         self.right = None
# #         self.data = val
# # def preOrder(root):
# #     if root != None:
# #         print(root.data,end = " ")
# #         preOrder(root.left)
# #         preOrder(root.right)
# # def inOrder(root):
# #     if root != None:
# #         inOrder(root.left)
# #         print(root.data,end = " ")
# #         inOrder(root.right)
# # def postOrder(root):
# #     if root != None:
# #         postOrder(root.left)
# #         postOrder(root.right)
# #         print(root.data,end = " ")
# # root = node(1)
# # root.left = node(3)
# # root.right = node(5)
# # root.left.left = node(2)
# # root.left.right = node(4)
# # root.right.right = node(8)
# # preOrder(root)
# # print()
# # inOrder(root)
# # print()
# # postOrder(root)
# # binary search tree
# class bst:
#     def __init__(self, val):
#         self.left = None
#         self.right = None
#         self.data = val

# def insertion(root, val):
#     if root is None:
#         return bst(val)
#     if root.data == val:
#         return root
#     if root.data > val:
#         root.left = insertion(root.left, val)
#     else:
#         root.right = insertion(root.right, val)
#     return root

# def search(root, val):
#     if root is None:
#         print("element not found")
#         return
#     if root.data == val:
#         print("element found")
#         return
#     if root.data > val:
#         search(root.left, val)
#     else:
#         search(root.right, val)

# def get_successor(root):
#     root = root.right
#     while root is not None and root.left is not None:
#         root = root.left
#     return root

# def get_predessor(root):
#     root = root.left
#     while root is not None and root.right is not None:
#         root = root.right
#     return root

# def delete(root, val):
#     if root is None:
#         return root
        
#     if root.data > val:
#         root.left = delete(root.left, val)
#     elif root.data < val:
#         root.right = delete(root.right, val)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         else:
#             suc = get_successor(root)
#             root.data = suc.data
#             root.right = delete(root.right, suc.data)
#     return root
            
# def inOrder(root):
#     if root is not None:
#         inOrder(root.left)
#         print(root.data, end=" ")
#         inOrder(root.right)

# root = insertion(None, 20)
# root = insertion(root, 15)
# root = insertion(root, 30)
# root = insertion(root, 45)
# root = insertion(root, 12)
# root = insertion(root, 18)
# root = insertion(root, 65)
# root = insertion(root, 26)
# root = insertion(root, 36)
# root = insertion(root, 55)
# inOrder(root)
# root = delete(root, 30) 
# print("\n")
# inOrder(root)