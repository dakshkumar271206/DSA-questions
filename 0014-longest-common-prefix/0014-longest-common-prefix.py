class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        strs.sort()
        fir = strs[0]
        las = strs[-1]
        for i in range(min(len(fir),len(las))):
            if fir[i] != las[i]:
                return fir[:i]
        return fir[:min(len(fir),len(las))]
        