class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = [[] for _ in range(numRows)]
        k = numRows - 1
        z = 0
        j = 0
        if numRows == 1:
            return s
        while(z < len(s)):
            k += 1
            # print(k, z)
            for i in range(numRows):
                if z >= len(s):
                    break
                if k == numRows:
                    # print(z)
                    a[i].append(s[z])
                    z += 1
                elif i == numRows - k:
                    a[i].append(s[z])
                    z += 1
                else:
                    a[i].append("")
                
            if k == numRows:
                k = 1
            j += 1

        s1 = ""

        for i in a:
            s1 += "".join(i)
        
        return s1
            

