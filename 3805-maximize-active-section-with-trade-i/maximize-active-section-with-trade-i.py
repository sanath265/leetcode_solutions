class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        a = []
        s = "1" + s + "1"
        ans = 0
        for i in range(len(s)):
            if s[i] == s[i-1]:
                ans += 1
            else:
                if s[i] == "0":
                    a.append(ans)
                else:
                    a.append(-ans)
                ans = 1
        
        a.append(ans)
        
        maxi = 0
        l = -1
        r = -1
        for i in range(len(a) - 3):
            if a[i] < 0 and a[i+2] < 0 and a[i+1] > 0:
                if abs(a[i] + a[i+2]) > maxi:
                    l = i
                    r = i+2
                    maxi = abs(a[i] + a[i+2])
        
        ans = 0
        for i in range(len(a)):
            if a[i] > 0 and i != l and i != r:
                ans += a[i]
        
        return ans + maxi -2
