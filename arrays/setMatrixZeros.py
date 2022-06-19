"""
Given an mxn integer matrix, if an element is 0, set its entire row and column to 0's
you must do it in place.
"""
    
#approach 1

#my soluution
class Solution:
    def setZeroes_approach1(self, matrix) -> None:
        """
        Do not return anything, modify matrix in place instead.
        """
        rows, cols = set(), set()

        m,n=len(matrix),len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    rows.add(row)
                    cols.add(col)

        for row in range(m):
            for col in range(n):
                if row in rows or col in cols:
                    matrix[row][col]=0




