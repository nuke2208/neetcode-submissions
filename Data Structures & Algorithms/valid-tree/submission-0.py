class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {}
        for i in range(n):
            graph[i] = []
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        checked = set()
        def dfs(node,parent):
            if node in checked:
                return False
            checked.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(checked) == n
        