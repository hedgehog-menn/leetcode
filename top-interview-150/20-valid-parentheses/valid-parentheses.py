class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
 
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        buff = []

        for i in range(len(s)):
            if s[i] in d:
                buff.append(d[s[i]])
            elif len(buff) == 0:
                return False
            elif buff[-1] == s[i]:
                buff.pop()
            else:
                return False

        return len(buff) == 0