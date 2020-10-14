from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r,c):
            visited = []
            stack = [(r,c)]
            switch = 0
            while stack:
                row,col = stack.pop()
                if row==0 or col==0 or row==len(board)-1 or col==len(board[0])-1:
                    switch=1
                if (row,col) not in visited:
                    visited.append((row,col))
                    if col<len(board[0])-1 and board[row][col+1]=='O':
                        stack.append((row,col+1))
                    if row<len(board)-1 and board[row+1][col]=='O':
                        stack.append((row+1,col))
                    if col>1 and board[row][col-1]=='O':
                        stack.append((row,col-1))
                    if row>1 and board[row-1][col]=='O':
                        stack.append((row-1,col))
            if switch==0:
                for (row,col) in visited:
                    board[row][col] = 'X'
            checked.extend(visited)

        checked = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in checked and board[i][j]=='O':
                    print((i,j))
                    dfs(i,j)
                    print('####')
        print(board)

input = list(read().rstrip().lstrip('[[').rstrip(']]').split('],['))
for i in range(len(input)):
    input[i] = input[i].split(',')
mod = Solution()
mod.solve(input)
