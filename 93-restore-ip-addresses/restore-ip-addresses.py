class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        output = []
        def dfs(string, index, dot):
            nonlocal output
            if dot > 3 and index >= len(s):
                output.append(string[1:])
            
            if index >= len(s) or dot > 3:
                return
            
            if check_string(s[index]):
                dfs(string + "." + s[index], index + 1, dot + 1)

            if index + 1 < len(s) and check_string(s[index: index+2]):
                dfs(string + "." + s[index: index+2], index + 2, dot + 1)
            
            if index + 2 < len(s) and check_string(s[index: index+3]):
                dfs(string + "." + s[index: index+3], index + 3, dot + 1)
            



        def check_string(s):
            if s[0] == '0' and s != '0':
                return False
            
            return 0 <= int(s) <= 255

        dfs("", 0, 0)
        return output


        
    