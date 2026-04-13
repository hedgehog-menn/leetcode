class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if num in d:
                return [d[num], index]
            else:
                d[target - num] = index
        return