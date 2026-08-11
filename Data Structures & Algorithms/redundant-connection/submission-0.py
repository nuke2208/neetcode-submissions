class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        n = len(edges)
        for i in range(n+1):
            graph[i] = []
        def dfs(node,parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour,node) is True:
                    return True
            return False
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            visited = set()
            if dfs(a,-1) is True:
                return[a,b]
        


           
        