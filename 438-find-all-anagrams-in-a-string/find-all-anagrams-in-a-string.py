class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = {}
        for i in p:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        b = {}
        ans = []
        for i in range(len(s)):
            if s[i] not in b:
                    b[s[i]] = 1
            else:
                b[s[i]] += 1
            
            if i >= len(p):
                if b[s[i-len(p)]] == 1:
                    del b[s[i-len(p)]]
                else:
                    b[s[i-len(p)]] -= 1

            
            if b == a:
                ans.append(i - len(p) + 1)
            
        return ans



        