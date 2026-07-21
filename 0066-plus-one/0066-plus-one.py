class Solution(object):
    def plusOne(self, digits):
        r = ''
        re = []
        for _ in range(len(digits)):
            r = r + str(digits[_])
        r = (str(int(r) + 1))
        for _ in r:
            re.append(int(_))
        return re
        