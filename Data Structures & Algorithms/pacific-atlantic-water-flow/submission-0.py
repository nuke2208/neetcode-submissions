class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        rows = len(heights)
        columns = len(heights[0])
        def reachespacific(r,c):
            visited = set()
            def dfs(r,c):
                if r==0 or c == 0:
                    return True
                if (r,c) in visited:
                    return False
                visited.add((r,c))
                if r>0 and heights[r-1][c] <= heights[r][c]:
                    if dfs(r-1,c) is True:
                        return True
                if c>0 and heights[r][c-1] <= heights[r][c]:
                    if dfs(r,c-1) is True:
                        return True
                if r < (rows - 1) and heights[r+1][c] <= heights[r][c]:
                    if dfs(r+1,c) is True:
                        return True
                if c < (columns - 1) and heights[r][c+1] <= heights[r][c]:
                    if dfs(r,c+1) is True:
                        return True
                return False
            return dfs(r,c)
        def reachatlantic(r,c):
            visited = set()
            def dfs(r,c):
                if r == rows - 1 or c == columns - 1:
                    return True
                if (r,c) in visited:
                    return False
                visited.add((r,c))
                if r > 0 and heights[r-1][c] <= heights[r][c]:
                    if dfs(r-1,c) is True:
                        return True
                if c>0 and heights[r][c-1] <= heights[r][c]:
                    if dfs(r,c-1) is True:
                        return True
                if c < columns - 1 and heights[r][c+1] <= heights[r][c]:
                    if dfs(r,c+1) is True:
                        return True
                if r < rows - 1 and heights[r+1][c] <= heights[r][c]:
                    if dfs(r+1,c) is True:
                        return True
                return False
            return dfs(r,c)
        for r in range(rows):
            for c in range(columns):
                if reachespacific(r,c) and reachatlantic(r,c):
                    result.append([r,c])
        return result
        
                    
                
        