class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        output = []
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] + 1 == nums[j + 1]:
                j += 1
            
            if  nums[i] == nums[j]:
                output.append(str(nums[i]))
            else:
                output.append("{}->{}".format(nums[i], nums[j]))
            
            i = j + 1

        return output
                
                
        