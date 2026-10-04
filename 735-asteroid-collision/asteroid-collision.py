class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []

        for i in asteroids:
            flag = 1
            if i < 0:
                while(stack):
                    if stack[-1] > 0:
                        if stack[-1] < abs(i):
                            stack.pop()
                        elif stack[-1] == abs(i):
                            stack.pop()
                            flag = 0
                            break
                        else:
                            flag = 0
                            break
                    else:
                        break
                if flag:
                    stack.append(i)
                    flag = 1

            else:
                stack.append(i)
        return stack
        