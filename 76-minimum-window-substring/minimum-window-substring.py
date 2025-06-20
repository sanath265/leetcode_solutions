class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        T = Counter(t)
        l = 0
        r = 0
        S = {}
        formed  = 0
        ans = (float('inf'), l, r)
        while(r < len(s)):
            if s[r] in T:
                if s[r] not in S:
                    S[s[r]] = 1
                else:
                    S[s[r]] += 1
                
                if T[s[r]] == S[s[r]]:
                    formed += 1
            
            # print(S, ans)
            
            while (l <= r and formed == len(T)):
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                if s[l] in T:
                    S[s[l]] -= 1

                    if s[l] in T and S[s[l]] < T[s[l]]:
                        formed  -= 1
                l += 1
            r+= 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


            

        
