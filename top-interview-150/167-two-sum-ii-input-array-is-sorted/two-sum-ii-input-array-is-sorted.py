class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(numbers):
            if n in hashmap:
                return [hashmap[n] + 1, i + 1]
            else:
                hashmap[target - n] = i