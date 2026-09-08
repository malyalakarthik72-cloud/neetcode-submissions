class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            seen1 = []
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val not in seen1:
                    seen1.append(val)
                else:
                    return False

        for j in range(9):
            seen2 = []
            for i in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val not in seen2:
                    seen2.append(val)
                else:
                    return False

        for r in range(0, 9, 3):       
            for c in range(0, 9, 3):   
                seen3 = []
                for i in range(r, r + 3):       
                    for j in range(c, c + 3):  
                        val = board[i][j]
                        if val == '.':
                            continue
                        if val not in seen3:
                            seen3.append(val)
                        else:
                            return False
        
        return True