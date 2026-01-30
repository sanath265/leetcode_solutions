class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        count = ""
        substr = ""
        ans = ""
        for i in s:

            if "0" <= i <= "9":
                count += i
            elif i == "[":
                if stack:
                    stack[-1][1] += substr
                else:
                    ans += substr
                substr = ""
                stack.append([count, ""])
                count = ""
            elif i == ']':
                last = stack.pop()
                push = ""
                if substr:
                    push += (last[1] + substr) * int(last[0])
                else:
                    push += int(last[0]) * last[1]
                if stack:
                    stack[-1][1] += push
                else:
                    # print("last:", last, substr)
                    ans += push
                substr = ""
            else:
                substr += i
            print(stack, ans)

        return ans + substr



        