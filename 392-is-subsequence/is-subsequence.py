class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        def sequence(l, r):

            if l == len(s):
                return True
            
            if r == len(t):
                return False
            
            if s[l] == t[r]:
                l +=1 
            r +=1 

            return sequence(l, r)

        return sequence(0, 0)