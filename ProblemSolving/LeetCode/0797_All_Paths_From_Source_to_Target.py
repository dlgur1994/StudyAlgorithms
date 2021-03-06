from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,ans):
            visited[node] = True
            if node == len(graph)-1:
                res.append(ans[:])
                return
            for child in graph[node]:
                ans.append(child)
                dfs(child,ans)
                ans.pop()

        visited = [False for i in range(len(graph))]
        res = []
        dfs(0,[0])
        return res

input = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
for i in range(len(input)):
    if len(input[i])==0:
        input[i] = []
        continue
    if len(input[i])==1:
        input[i] = list(map(int,input[i]))
        continue
    input[i] = list(map(int,input[i].split(',')))
mod = Solution()
print(mod.allPathsSourceTarget(input))
