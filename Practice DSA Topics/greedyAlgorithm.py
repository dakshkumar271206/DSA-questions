# # wap to find the min. and max. of the diffence between two arrays,
# # which is made from the big array inputed by the user.
# def min_max_diff(arr):
#     arr.sort()
#     n = len(arr)
#     m = n//2
#     max, min, j = 0,0,-1
#     for i in range(m):
#         max = max + abs(arr[i] - arr[j])
#         j-=1
#         min = min + abs(arr[2*i] - arr[2*1+1])
#     print("max. difference:-> ", max)
#     print("min. difference:-> ",min)
# ar = [12,5,25,10,2,15,8,30]
# min_max_diff(ar)
# time O(n)
# find min. no. of denominations
# [1,2,5,10,20,50,100,200,500]
# def denominations(amt,arr):
#     arr.sort()
#     camt = 0
#     i = -1
#     cnt = 0
#     while amt != 0:
#         for _ in range(len(arr)):
#             while amt >= arr[i]:
#                 camt = arr[i]
#                 amt = amt - camt
#                 cnt+=1
#             i-=1
#     print("no. of coins :-> ", cnt)
# ar = [1,2,5,10,20,50,100,200,500]
# amt = 1024
# denominations(amt,ar)
# time = O(n.log n + A)