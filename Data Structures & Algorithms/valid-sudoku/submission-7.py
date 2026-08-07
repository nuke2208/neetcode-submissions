class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
        for j in range(9):
            seen = set()
            for i in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
        for startrow in range(0,9,3):
            for startcol in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[startrow + i][startcol + j]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        else:
                            seen.add(num)
        return True           