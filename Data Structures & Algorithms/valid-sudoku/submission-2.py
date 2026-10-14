class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # [r][c]
        # r pass, digits dont duplicate 1-9
        # c pass, digits don't duplicate 1-9
        # at every multiple of 3, r = c, subgrid has no duplicates 1-9

        for r in range(0, 9):
            seen = set()
            for i in range(0, 9):
                s = board[r][i]
                if s in seen:
                    return False
                elif s == '.':
                    continue
                seen.add(s)

        for c in range(0, 9):
            seen = set()
            for i in range(0, 9):
                s = board[i][c]
                if s in seen:
                    return False
                elif s == '.':
                    continue
                seen.add(s)

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        s = board[i + r][j + c]
                        if s in seen:
                            return False
                        elif s == '.':
                            continue
                        seen.add(s)
        
        return True
