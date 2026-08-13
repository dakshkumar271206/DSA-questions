# # we are given n items with {weight, value} of each item
# # and the capacity of knapsack(bori)W. we need to put these 
# # items in the knapsack such that the final value of the items 
# # in the knapsack is maximum. (fractional knapsack problem:-> greeedy approach)
# def Fractional_knapsack(item_wgt, price, capacity):
#     n = len(item_wgt)
#     item = [(price[_], item_wgt[_], price[_]/item_wgt[_]) for _ in range(n)] #(total price,total weight,price per kg)
#     for _ in range(n):
#         for i in range(_+1, n):
#             if item[_][2]<item[i][2]:
#                 item[_], item[i] = item[i], item[_]
#     profit = 0.0
#     for price, item_wgt, perKgPrice in item:
#         if capacity >= item_wgt:
#             capacity = capacity - item_wgt
#             profit = profit + price
#         else:
#             profit = profit + perKgPrice*capacity
#     print("total profit:--> ", profit)
# item_wt = [7,3,4,5]
# capa = 20
# price = [24,21,12,10]
# Fractional_knapsack(item_wt, price,capa)