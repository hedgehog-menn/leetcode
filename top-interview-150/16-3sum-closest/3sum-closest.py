class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if abs(target - sum) < abs(target - closet):
                    closet = sum

                if closet == target:
                    return target
                elif sum < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return closet
        