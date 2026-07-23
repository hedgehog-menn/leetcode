class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(numbers):
            if n in hashmap:
                return [hashmap[n] + 1, i + 1]

            hashmap[target - n] = i