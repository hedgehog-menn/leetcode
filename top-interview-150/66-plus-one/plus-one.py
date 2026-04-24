class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier, digits[-1] = divmod(digits[-1] + 1, 10)
        pointer = 2

        while carrier == 1:
            if pointer > len(digits):
                digits.insert(0, 1)
                carrier = 0
            else:
                carrier, digits[-pointer] = divmod(digits[-pointer] + 1, 10)
            pointer += 1

        return digits