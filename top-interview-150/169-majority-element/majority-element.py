class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        max_num = 1
        nums.sort()

        counting_num = nums[0]
        majority = nums[0]

        for  i in range(len(nums)):
            if nums[i] == counting_num:
                count += 1
            else:
                count = 1
                counting_num = nums[i]

            if count > max_num:
                max_num = count
                majority = nums[i]

        return majority