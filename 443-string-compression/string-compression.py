class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev = 0
        ans = 0
        pos = 0
        for i in range(1, len(chars)):
            if chars[i] != chars[prev]:
                # ans = 
                # print(pos, i, prev, chars)
                chars[pos] = chars[i-1]
                pos+=1
                if i - prev > 1:
                    n = i - prev
                    strpos = pos + len(str(n))
                    while(n > 0):
                        strpos -= 1
                        chars[strpos] = str(n % 10)
                        n = n//10
                        pos+=1
                # pos += 1
                prev = i
        chars[pos] = chars[len(chars)-1]
        pos+=1
        # print(prev)
        if len(chars) - prev > 1:
            n = len(chars) - prev
            strpos = pos + len(str(n))
            while(n > 0):
                strpos -= 1
                chars[strpos] = str(n % 10)
                n = n//10
                pos+=1
            # pos += 1

        return pos





        