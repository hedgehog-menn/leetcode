class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s_nums = sorted(set(nums))
        prev = s_nums[0]
        longest = 1
        counter = 1

        for i in range(1, len(s_nums)):
            if s_nums[i] == prev + 1:
                prev = s_nums[i]
                counter += 1
            else:
                longest = max(counter, longest)
                counter = 1
                prev = s_nums[i]

        longest = max(counter, longest)
        return longest
