class Solution(object):
    def isValid(self, s):
        st = []
        map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char not in map:
                st.append(char)
            if char in map:
                if len(st) == 0:
                    return False
                if len(st) > 0:
                    top = st.pop()
                    if map[char] != top:
                        return False
        if len(st) == 0:
            return True
        if len(st) > 0:
            return False