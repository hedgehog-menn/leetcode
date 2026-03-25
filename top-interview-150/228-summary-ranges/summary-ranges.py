class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        first_of_range = nums[0]
        output = []
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                if i == len(nums) - 2:
                    output.append(str(first_of_range) + "->" + str(nums[-1]))
            elif first_of_range == nums[i]:
                output.append(str(nums[i]))
                first_of_range = nums[i+1]
            else:
                output.append(str(first_of_range) + "->" + str(nums[i]))
                first_of_range = nums[i+1]

        if first_of_range == nums[-1]:
            output.append(str(nums[-1]))
            

        return output
            
        