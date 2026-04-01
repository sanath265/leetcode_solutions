class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        health = {}

        sort = sorted(positions)

        for i in range(len(positions)):
            health[positions[i]] = [healths[i], directions[i]]
        # print(sort)
        stack = []
        for i in sort:

            r2 = health[i]

            while(stack):
                index = stack[-1]
                r1 = health[index]

                b = False
                # print(r1, r2)
                if r1[1] == "R" and r2[1] == "L":
                    if r1[0] > r2[0]:
                        health[index] = [health[index][0]-1, health[index][1]]
                        health[i] = [0, health[i][1]]
                        
                        b = True
                        break
                    elif r1[0] < r2[0]:
                        health[index] = [0, health[index][1]]
                        health[i] = [health[i][0]-1, health[i][1]]
                        r2 = health[i]
                        stack.pop()
                    else:
                        health[index] = [0, r1[1]]
                        health[i] = [0, r2[1]]
                        stack.pop()
                        b = True
                else:
                    break
                # print(stack)
                
                if b:
                    break
            if health[i][0] > 0:
                    stack.append(i)
        ans = []
        for i in positions:
            if health[i][0] > 0:
                ans.append(health[i][0])
        # print(health)
        
        return ans