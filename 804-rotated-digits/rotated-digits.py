class Solution:
    def rotatedDigits(self, n: int) -> int:
        c = 0
        for i in range(1, n+1):
            number = str(i)
            # print("2" in number, number)
            if "3" in number or "4" in number or "7" in number:
                continue
            if "5" in  number or "6" in  number or "2" in  number or "9" in  number:            
                # print(number)
                c += 1
            
        
        return c