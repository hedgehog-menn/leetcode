class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: 
            return 0

        l, r = 1, x
        res = 0

        while l <= r:
            m = (l + r) // 2
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
                res = m
            else:
                return m

        return res
        