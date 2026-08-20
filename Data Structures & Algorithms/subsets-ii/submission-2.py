class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = set()

        def dfs(index,arr):
            if index == n:
                answer.add(tuple(sorted(arr)))
                return
            arr.append(nums[index])
            dfs(index+1,arr)
            arr.pop()
            dfs(index+1,arr)
        dfs(0,[])
        return [list(i) for i in answer]

        