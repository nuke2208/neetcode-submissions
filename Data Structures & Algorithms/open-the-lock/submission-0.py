from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        visited = set()
        if "0000" in deads:
            return -1
        q = deque(["0000"])
        visited.add("0000")
        steps = 0
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current == target:
                    return steps
                for i in range(4):
                    digit = int(current[i])
                    up = (digit + 1)%10
                    down = (digit - 1)%10
                    nextup = current[:i] + str(up) + current[(i+1):]
                    nextdown = current[:i] + str(down) + current[(i+1):]
                    if nextup not in deads and nextup not in visited:
                        visited.add(nextup)
                        q.append(nextup)
                     
                    if nextdown not in deads and nextdown not in visited:
                        visited.add(nextdown)
                        q.append(nextdown)
            steps += 1
        return -1
    
        