class Solution:
    def intToRoman(self, num: int) -> str:
        
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        i = 0
        ans = ""
        while(num > 0):
            if num < number[i]:
                i+=1
                continue
            # print(num, ans, number[i], roman[i])
            j = num // number[i]
            num = num % number[i]
            while(j > 0):
                j -= 1
                ans += roman[i]
        
        return ans
            

