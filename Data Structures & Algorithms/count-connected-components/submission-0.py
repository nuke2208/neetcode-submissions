class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count



        