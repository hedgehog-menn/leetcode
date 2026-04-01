class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = s
        result = 0
        if "IV" in roman:
            result += 4
            roman = roman.replace("IV", "")
        if "IX" in roman:
            result += 9
            roman = roman.replace("IX", "")
        if "XL" in roman:
            result += 40
            roman = roman.replace("XL", "")
        if "XC" in roman:
            result += 90
            roman = roman.replace("XC", "")
        if "CD" in roman:
            result += 400
            roman = roman.replace("CD", "")
        if "CM" in roman:
            result += 900
            roman = roman.replace("CM", "")

        result += roman.count("I") + roman.count("V")*5 + roman.count("X")*10 + roman.count("L")*50 + roman.count("C")*100 + roman.count("D")*500 + roman.count("M")*1000

        return result