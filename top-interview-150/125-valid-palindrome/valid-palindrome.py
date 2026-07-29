class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
