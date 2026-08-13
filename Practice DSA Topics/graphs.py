# # class graphbymatrix:
# #     def __init__(self,vertex):
# #         self.mat = [[0] * vertex for _ in range(vertex)]
# #         self.size = vertex
# #     def add_edge(self,src,des):#source, destination as src and des
# #         if 0<= src < self.size and 0<= des < self.size:
# #             self.mat[src][des] = 1
# #             #undirected graphs then this code is executed
# #             self.mat[src][des] = 1
# #         else:
# #             print("invaild edge.")
# #     def Print(self):
# #         for row in self.mat:
# #             print(' '.join(map(str,row)))
# # g = graphbymatrix(5)
# # g.add_edge(0,1)
# # g.add_edge(0,2)
# # g.add_edge(1,3)
# # g.add_edge(2,4)
# # g.Print()
# # class graphbylist:
# #     def __init__(self):
# #         self.adjList = {}
# #     def add_vertex(self, vertex):
# #         if vertex  not in self.adjList:
# #             self.adjList[vertex] = []
# #     def addEdge(self,src,dest):
# #         self.add_vertex(src)
# #         self.add_vertex(dest)
# #         self.adjList[src].append(dest)
# #         self.adjList[dest].append(src)
        
# #     def printGraph(self):
# #         for _ in self.adjList:
# #             print(_, " ---> ", self.adjList[_], end = '\n')
# # G = graphbylist()
# # G.addEdge(1,2)
# # G.addEdge(2,3)
# # G.addEdge(1,4)
# # G.addEdge(4,3)
# # G.addEdge(2,4)
# # G.addEdge(4,5)
# # G.addEdge(3,5)
# # G.printGraph()
# # class graphbymatrix:
# #     def __init__(self,vertex):
# #         self.mat = [[0] * vertex for _ in range(vertex)]
# #         self.size = vertex
# #     def add_edge(self,src,des):#source, destination as src and des
# #         if 0<= src < self.size and 0<= des < self.size:
# #             self.mat[src][des] = 1
# #             #undirected graphs then this code is executed
# #             self.mat[src][des] = 1
# #         else:
# #             print("invaild edge.")
# #     def Print(self):
# #         for row in self.mat:
# #             print(' '.join(map(str,row)))
# #     def dfs(self, src):
# #         visited = [False] * self.size
# #         stack = [src]
# #         while stack:
# #             v = stack.pop()
# #             if visited[v] == False:
# #                 print(v, end = '--->')
# #                 visited[v] = True
# #             for _ in range(self.size):
# #                 if self.mat[v][_] == 1:
# #                     stack.append(_)
# # g = graphbymatrix(6)
# # g.add_edge(0,1)
# # g.add_edge(0,2)
# # g.add_edge(2,3)
# # g.add_edge(2,4)
# # g.add_edge(3,5)
# # g.add_edge(4,5)
# # g.dfs(0)
# from collections import deque
# class graphbymatrix:
#     def __init__(self,vertex):
#         self.mat = [[0] * vertex for _ in range(vertex)]
#         self.size = vertex
#     def add_edge(self,src,des):#source, destination as src and des
#         if 0<= src < self.size and 0<= des < self.size:
#             self.mat[src][des] = 1
#             #undirected graphs then this code is executed
#             self.mat[src][des] = 1
#         else:
#             print("invaild edge.")
#     def Print(self):
#         for row in self.mat:
#             print(' '.join(map(str,row)))
#     def bfs(self,src):
#         visited = [False] * self.size
#         q = deque([src])
#         visited[src] = True
#         while q:
#             v = q.popleft()
#             print(v, end = "-->")
#             for _ in range(self.size):
#                 if self.mat[v][_] == 1 and visited[_] == False:
#                     visited[_] = True
#                     q.append(_)
# g = graphbymatrix(8)
# g.add_edge(0,1)
# g.add_edge(0,3)
# g.add_edge(1,3)
# g.add_edge(3,5)
# g.add_edge(3,4)
# g.add_edge(4,5)
# g.add_edge(4,6)
# g.add_edge(6,2)
# g.add_edge(6,7)
# g.bfs(0)