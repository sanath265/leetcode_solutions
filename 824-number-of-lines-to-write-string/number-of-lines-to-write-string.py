class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        lines = 0
        currentWidth = 0
        for i in s:
            currentWidth += widths[ord(i) - ord('a')]

            if currentWidth > 100:
                lines+=1
                currentWidth = widths[ord(i) - ord('a')]
        
        return [lines + 1, currentWidth]