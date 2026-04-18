class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        copy = matrix.copy()

        for i in range(n):
            matrix[i] = [copy[j][i] for j in reversed(range(n))]
