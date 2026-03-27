class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        # correct, but still too long
        for i in range(len(numbers)):
            j = i + 1

            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                elif numbers[i] + numbers[j] > target:
                    break
                else:
                    j += 1
        """

        i = 0
        j = len(numbers) - 1

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            if sum < target:
                i += 1
            if sum > target:
                j -= 1
