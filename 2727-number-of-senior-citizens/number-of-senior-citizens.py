class Solution:
    def countSeniors(self, details: List[str]) -> int:
        if len(details) == 0:
            return 0

        if int(details[0][11:13]) > 60:
            return self.countSeniors(details[1:]) + 1
        else:
            return self.countSeniors(details[1:])