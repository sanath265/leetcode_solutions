class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == '1' and s[i+1] == '1':
                continue
            elif s[i] == "1":
                count += 1
        return count == 1
        