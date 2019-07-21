#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 36. Valid Sudoku
class Solution(object):
    def isValidSudoku(self, board):
        col = [[] for _ in range(9)]
        block = [[] for _ in range(9)]
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row.append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in col[j]:
                        col[j].append(board[i][j])
                    else:
                        return False
                    num = 3*(j//3) + i//3
                    if board[i][j] not in block[num]:
                        block[num].append(board[i][j])
                    else:
                        return False
        return True
            

