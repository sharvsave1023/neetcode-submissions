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

        # 0, 1, 2 -> 0 
        # 3, 4, 5 -> 1 
        # 6, 7, 8 -> 2 
        # floor division for col

        # 0, 1, 2 -> 0
        # 3, 4, 5 -> 1
        # 6, 7, 8 -> 2
        # floor division for col

        blocks = defaultdict(set)

        for r in range(0, 9):
            for c in range(0, 9):
                
                block_num = r // 3 * 3 + c // 3
                s = board[r][c]
                if s == ".": 
                    continue 
                if s in blocks[block_num]:
                    return False 
                blocks[block_num].add(s)
        
        return True
