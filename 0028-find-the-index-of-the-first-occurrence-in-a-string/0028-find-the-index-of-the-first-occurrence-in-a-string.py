class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        l = len(haystack) - len(needle) + 1
        for i in range(l):
            ch = haystack[i:i+len(needle)]
            if ch == needle:
                return i
        return -1