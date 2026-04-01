class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        
        for i in range(1, len(s)):
            result = result - roman_dict[s[i - 1]] if roman_dict[s[i - 1]] < roman_dict[s[i]] else result + roman_dict[s[i - 1]]

        result += roman_dict[s[len(s) -1]]

        return result