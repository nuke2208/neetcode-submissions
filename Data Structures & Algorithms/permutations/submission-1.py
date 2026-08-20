class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        answer = []
        def dfs(k,arr,visited,perms):
            if k == 0:
                answer.append(perms.copy())
                return
            for i in range(n):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    perms.append(nums[i])
                    dfs(k-1,arr,visited,perms)
                    visited.remove(nums[i])
                    perms.pop()
        dfs(n,nums,visited,[])
        return answer

        
        

            
        