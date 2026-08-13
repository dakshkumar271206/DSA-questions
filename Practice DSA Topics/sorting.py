# decreasing order bubble sorting
# def bubbleDO(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] <= arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     return arr

# increasing order bubble sorting
# def bubbleIO(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] >= arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     return arr
# print('the increasing order sorting:-->',bubbleIO(arr))
# print('the decreasing order sorting:-->',bubbleDO(arr))

# # decreasing order selection sorting 
# def selectionDO(arr):
#     # max element searching method
#     n = len(arr)
#     for i in range(n):
#         max = i
#         for j in range(i,n):
#             if arr[max] <= arr[j]:
#                 max = j
#         arr[i], arr[max] = arr[max], arr[i]
#     return arr

# # increasing order selection sorting
# def selectionIO(arr):
#     # min element searching method
#     n = len(arr)
#     for i in range(n):
#         mini = i
#         for j in range(i,n):
#             if arr[mini] >= arr[j]:
#                 mini = j
#         arr[i], arr[mini] = arr[mini], arr[i]
#     return arr

# # decreasing order insertion sorting 
# def insertionDO(arr):
#     n = len(arr)
#     for i in range(1,n):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key > arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
            
#     return arr
# # increasing order insertion sorting
# def insertionIO(arr):
#     n = len(arr)
#     for i in range(1,n):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#     return arr

# # increasing order merge sorting
# def divideIO(arr, l, r):
#     if l < r:
#         m = (l + r) // 2
#         divideIO(arr, l, m)
#         divideIO(arr, m + 1, r)
#         mergeIO(arr, l, m, r)
# def mergeIO(arr, l, m, r):
#     s1 = m - l + 1
#     s2 = r - m
#     L = [0] * s1
#     R = [0] * s2
#     for _ in range(s1):
#         L[_] = arr[l + _]
#     for i in range(s2):
#         R[i] = arr[m + 1 + i]
#     i = j = 0
#     k = l
#     while i < s1 and j < s2:
#         if L[i] < R[j]:
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#             k += 1  # Fixed: changed the second j+=1 to k+=1
#     while i < s1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < s2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
# # decreasing order merge sorting
# def divideDO(arr, l, r):
#     if l < r:
#         m = (l + r) // 2
#         divideDO(arr, l, m)
#         divideDO(arr, m + 1, r)
#         mergeDO(arr, l, m, r)
# def mergeDO(arr, l, m, r):
#     s1 = m - l + 1
#     s2 = r - m
#     L = [0] * s1
#     R = [0] * s2
#     for _ in range(s1):
#         L[_] = arr[l + _]
#     for i in range(s2):
#         R[i] = arr[m + 1 + i]
#     i = j = 0
#     k = l
#     while i < s1 and j < s2:
#         if L[i] > R[j]:
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     while i < s1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < s2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# # increasing order quick sorting
# def quickIO(arr, l, r):
#     if l < r:
#         p = partition_IO(arr, l, r)
#         quickIO(arr, l, p-1)
#         quickIO(arr, p+1, r)
# def partition_IO(arr, l, r):
#     pivot = arr[l]
#     i = l + 1
#     j = r
#     while True:
#         while i <= j and arr[i] < pivot:
#             i += 1
#         while i <= j and arr[j] > pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[l], arr[j] = arr[j], arr[l]
#     return j
# # decreasing order quick sorting
# def quickDO(arr, l, r):
#     if l < r:
#         p = partition_DO(arr, l, r)
#         quickDO(arr, l, p-1)
#         quickDO(arr, p+1, r)

# def partition_DO(arr, l, r):
#     pivot = arr[l]
#     i = l + 1
#     j = r
#     while True:
#         while i <= j and arr[i] > pivot:
#             i += 1
#         while i <= j and arr[j] < pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[l], arr[j] = arr[j], arr[l]
#     return j

# ar = [5, 69, 2, 86, 69, 86, 349, 246, 316]
# quickIO(ar, 0, len(ar) - 1)
# print('the increasing order sorting:-->', ar)
# quickDO(ar, 0, len(ar) - 1)
# print('the decreasing order sorting:-->', ar)

# #divide and conque
# # finding min. and max. using D&C
# def min_max(arr, start, end):
#     if start == end:
#         return arr[start], arr[end]
#     if start+1 == end:
#         if arr[start] < arr[end]:
#             return arr[start], arr[end]
#         else:
#             return arr[end], arr[start]
#     m = (start + end)//2
#     min1, max1 = min_max(arr, start, m)
#     min2, max2 = min_max(arr, m+1, end)
#     return min(min1, min2), max(max1, max2)

# ar = [26,3,35,99,66,2,36,45,100,1,6,69,0]
# Min, Max = min_max(ar, 0, len(ar)-1)
# print(Min, Max)