class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)

        while True:
            sum_sqr = 0
            for digit in str_n:
                sum_sqr += int(digit) ** 2
            if sum_sqr == 1:
                return True
            elif sum_sqr == 4:
                return False

            str_n = str(sum_sqr)