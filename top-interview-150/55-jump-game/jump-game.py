class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        goal = len(nums) - 1

        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i >= goal:
                goal = i

        # able to be back at the first index
        return goal == 0

        
        