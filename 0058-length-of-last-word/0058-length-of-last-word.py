class Solution(object):
    def lengthOfLastWord(self, s):
        l = 0
        for i in range(len(s)-1, -1 ,-1):
            if s[i] != " ":
                l += 1
            elif l > 0:
                break
        return l