class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = max_jump = last_jump = jumps = 0

        while last_jump < len(nums) - 1:
            max_jump = max(max_jump, i + nums[i])
            if i == last_jump:
                last_jump = max_jump
                jumps += 1
            i += 1

        return jumps
        