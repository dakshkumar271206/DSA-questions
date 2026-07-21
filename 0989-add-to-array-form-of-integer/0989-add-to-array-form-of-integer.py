class Solution(object):
    def addToArrayForm(self, num, k):
        r = ''
        re = []
        for _ in range(len(num)):
            r = r + str(num[_])
        r = str(int(r) + k)
        for _ in r:
            re.append(int(_))
        return re
        