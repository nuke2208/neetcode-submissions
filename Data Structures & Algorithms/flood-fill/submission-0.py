from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        q = deque()
        q.append((sr,sc))
        temp = image[sr][sc]
        if temp == color:
            return image
        image[sr][sc] = color
        while q:
            r,c = q.popleft()
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == temp:
                    image[nr][nc] = color
                    q.append((nr,nc))
        return image