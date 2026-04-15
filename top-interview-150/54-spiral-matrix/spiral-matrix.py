class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, btm = 0, len(matrix)
        
        while left < right and top < btm:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, btm):
                result.append(matrix[i][right - 1])
            right -= 1
            
            # when it ends
            if not (left < right and top < btm):
                break

            for i in range(right - 1, left - 1, -1):
                result.append(matrix[btm - 1][i])
            btm -= 1

            for i in range(btm - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
        return result