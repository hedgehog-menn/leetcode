class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: 
            return x

        # considering the equation values 
        y = x
        z = (y + (x/y)) / 2

        while abs(y - z) >= 1:
            y = z
            z = (y + (x/y)) / 2

        return int(z)
        