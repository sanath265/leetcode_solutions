class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        area = 0

        stack = [-1]

        for i in range(len(heights)):
            
            while(stack[-1] != -1 and heights[stack[-1]] > heights[i]):
                j = stack.pop()
                k = stack[-1]
                area = max(area, heights[j] * (i - k - 1))
            area = max(area, heights[i])

            stack.append(i)  
        
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            area = max(area, current_height * current_width)
        return area   
            