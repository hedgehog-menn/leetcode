class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, n):
            result = 1.0
            while n:
                if n % 2 == 1:
                    result *= x
                x *= x
                n //= 2
            return result
        
        if n < 0:
            x = 1 / x
            n = -n
        
        return fast_pow(x, n)
        