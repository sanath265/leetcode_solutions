class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        

        def search(s):
            i = 0

            while(i < len(s)):
                j = 0
                if s[i] == part[0]:
                    j = searchPart(s, i)
                if j == len(part):
                    string = s[:i] + s[i+len(part):]
                    print(string)
                    return search(string)
            
                i+=1
            return s
        
        def searchPart(s, i):
            j = 0
            while(j < len(part)):
                if i+j < len(s) and part[j] == s[i + j]:
                    # print(part[j])
                    j += 1
                else:
                    break
            print(j)
            print(j)
            return j
            

        return search(s)
                
