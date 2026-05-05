class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < 2:
            return s

        rows = [""] * numRows
        s_pointer = 0
        row_pointer = 0

        while s_pointer < len(s):
            while s_pointer < len(s) and row_pointer < numRows:
                rows[row_pointer] += s[s_pointer]
                s_pointer += 1
                row_pointer += 1

            row_pointer = numRows - 2

            while s_pointer < len(s) and row_pointer > 0:
                rows[row_pointer] += s[s_pointer]
                s_pointer += 1
                row_pointer -= 1

        return "".join(rows)
        