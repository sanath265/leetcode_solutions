class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        # unique = 0
        # a = set()
        # for i in s:
        #     if i not in a:
        #         unique += 1
        #         a.add(i)
        
        # ans = ""
        # def rec(i, curr, vis):
        #     nonlocal ans

        #     if len(curr) == unique:
        #         # print(curr)
        #         if ans == "":
        #             ans = curr
        #         else:
        #             ans = min(ans, curr)
        #         return
        #     if i >= len(s):
        #         return 

        #     rec(i+1, curr, vis)
        #     # print(vis)
        #     if not vis[ord(s[i]) - ord('a')]:
        #         vis[ord(s[i]) - ord('a')] = True
        #         rec(i+1, curr+s[i], vis)
        #         vis[ord(s[i]) - ord('a')] = False
            

        # rec(0, "", [False for _ in range(26)])

        # return ans


        vis = [0] * 26
        num = [0] * 26

        unique = 0
        for i in s:
            num[ord(i) - ord('a')] += 1

        stk = []
        for i in s:
            index = ord(i) - ord('a')
            
            num[index] -= 1
            if vis[index] == 1:
                continue
            
            while(stk and i < stk[-1]):
                topIndex = ord(stk[-1]) - ord('a')
                if num[topIndex] > 0:
                    stk.pop()
                    vis[topIndex] = 0
                else:
                    break
            stk.append(i)
            vis[index] = 1
        
        return "".join(stk)
            
