# def removeElement(nums, val):
#         # 'k' acts as our placement pointer
#                 k = 0 
        
#         # 'i' acts as our reading pointer
#                 for i in range(len(nums)):
#         # If we find a number we want to KEEP
#                         if nums[i] != val:
#                 # Move it to the front at position 'k'
#                                 nums[k] = nums[i]
#                 # Increment 'k' for the next valid number
#                         k += 1
                
#         # LeetCode requires you to return the new length of valid elements
#                 return k
# l = [0,2,3,68,96,97,98,99,68]
# print(removeElement(l,68))
# print(l)