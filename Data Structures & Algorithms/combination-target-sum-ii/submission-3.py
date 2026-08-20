class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)
        candidates.sort()
        total = 0
        def dfs(index,path,total):
            if total == target:
                answer.append(path.copy())
                return
            if total > target:
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1,path,total+candidates[i])
                path.pop()
        dfs(0,[],0)
        return answer

        
        