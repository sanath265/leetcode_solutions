class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = int("".join(list(map(str, digits))))
        return list(map(int, list(str(a+1))))
        