class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {}

        l = 0
        r = 0
        maxi = 0

        while (l <= r and r < len(s)):
            if s[r] in a:
                a[s[r]] += 1
            else:
                a[s[r]] = 1
            
            while(a[s[r]] > 1):
                a[s[l]] -= 1
                l += 1
            maxi = max(maxi, r - l + 1)
            r+=1
        return maxi

        