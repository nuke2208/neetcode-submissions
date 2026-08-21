class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def dfs(left,right,arr):
            if left == n and right == n:
                answer.append(arr)
                return
            if left < n:
                dfs(left+1,right,arr + '(')
            if right < left:
                dfs(left,right+1,arr+')')
        dfs(0,0,"")
        return answer

        