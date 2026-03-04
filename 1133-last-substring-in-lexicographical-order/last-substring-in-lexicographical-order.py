class Solution:
    def lastSubstring(self, s: str) -> str:

        l = 0
        r = len(s) - 1

        ans = ""
        currentS = ""
        while(r >= 0):
            currentS = s[r] + currentS
            if currentS > ans:
                ans = currentS
            r-=1
            
        return ans

        