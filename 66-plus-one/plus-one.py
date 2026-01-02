class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits
        i = len(digits) - 1
        res = 10
        while(res > 9 and i >= 0):
            res = digits[i] + 1
            if res == 10:
                digits[i] = 0
            else:
                digits[i] = res
            i -= 1
  
        if i == -1 and res == 10:
            digits = [1] + digits
        
        return digits

        