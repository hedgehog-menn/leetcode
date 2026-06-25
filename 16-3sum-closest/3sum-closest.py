class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if abs(target - cur_sum) < abs(target - closet):
                    closet = cur_sum

                if cur_sum < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif cur_sum > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    return cur_sum

        return closet