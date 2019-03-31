"""
"""

from typing import *

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        clusters = []

        for rowIndex, row in enumerate(A):

            for columnIndex, box in enumerate(row):
                if box == 1:
                    neighboringLands = self.getNeighboringLand(A, rowIndex, columnIndex)
                    
                    for land in neighboringLands:
                        
        
    def getNeighboringLand(self, A: List[List[int]], row: int, column: int):
        res = []

        if row - 1 >= 0:
            if A[row - 1][column] == 1:
                res.append((row - 1, column))
        if column - 1 >= 0:
            if A[row][column] == 1:
                res.append((row, column - 1))
        if row + 1 <= len(A) - 1:
            if A[row + 1][column] == 1:
                res.append((row + 1, column))
        if column + 1 <= len(A[0]) - 1:
            if A[row][column + 1] == 1:
                res.append((row, column + 1))

        return res