class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        start_idx = 0
        if s[0] == '-':
            sign = -1
            start_idx = 1
        elif s[0] == '+':
            start_idx = 1
        result = 0
        for i in range(start_idx, len(s)):
            if not s[i].isdigit():
                break
            result = (result * 10) + int(s[i])
        result *= sign
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if result > MAX_INT:
            return MAX_INT
        if result < MIN_INT:
            return MIN_INT
        return result