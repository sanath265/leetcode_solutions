class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        c = {}
        d = set()
        for i in range(len(s)):
            if s[i] not in c:
                if t[i] not in d:
                    c[s[i]] = t[i]
                    d.add(t[i])
                else:
                    return False
            else:
                if c[s[i]] != t[i]:
                    return False
        return True