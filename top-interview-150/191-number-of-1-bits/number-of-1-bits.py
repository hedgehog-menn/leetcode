class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = f"{n:02b}"
        return binary.count("1")
        