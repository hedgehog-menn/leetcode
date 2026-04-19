class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_columns = set()
        for i, row in enumerate(matrix):
            zero_cells = [index for index, x in enumerate(row) if x == 0]
            if len(zero_cells) > 0:
                zero_columns.update(zero_cells)
                matrix[i] = [0 for _ in range(len(row))]

        for zero_column in zero_columns:
            for j in range(len(matrix)):
                matrix[j][zero_column] = 0
