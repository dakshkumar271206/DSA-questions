class Solution(object):
    def reverse(self, x):
        # Determine the sign and work with a positive number
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        rev = 0
        
        while x != 0:
            digit = x % 10
            x = x // 10
            
            # OVERFLOW PREDICTION: 
            # If rev is already greater than 214748364, the next step (rev * 10) 
            # will guarantee an overflow (e.g., creating 9646324350), so we return 0.
            if rev > 214748364 or (rev == 214748364 and digit > 7):
                return 0
                
            rev = (rev * 10) + digit
            
        return rev * sign