class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans= ord('z') + 1

        for i in letters:
            if i > target and ord(i) < ans:
                ans = ord(i)
                # ans = i
            # elif abs(ord(i) - ord(target)) == abs(ord(i) - ord(ans)) and i < ans:
            #     ans  = i
        if ans == ord('z') + 1:
            return letters[0]
        return chr(ans)