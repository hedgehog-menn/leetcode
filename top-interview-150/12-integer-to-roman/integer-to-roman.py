class Solution:
    def intToRoman(self, num: int) -> str:
        num_M, num = divmod(num, 1000)
        num_CM, num = divmod(num, 900)
        num_D, num = divmod(num, 500)
        num_CD, num = divmod(num, 400)
        num_C, num = divmod(num, 100)
        num_XC, num = divmod(num, 90)
        num_L, num = divmod(num, 50)
        num_XL, num = divmod(num, 40)
        num_X, num = divmod(num, 10)
        num_IX, num = divmod(num, 9)
        num_V, num = divmod(num, 5)
        num_IV, num = divmod(num, 4)
        num_I, num = divmod(num, 1)

        return num_M*"M" + num_CM*"CM" + num_D*"D" + num_CD*"CD" + num_C*"C" + num_XC*"XC" + num_L*"L" + num_XL*"XL" + num_X*"X" + num_IX*"IX" + num_V*"V" + num_IV*"IV" + num_I*"I"
        