class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m = 0
        c = 0
        for i in s:
            if i == " ":
                if c > 0:
                    m = c
                    c = 0
            else:
                c += 1

        if c == 0:
            return m
        else:
            return c