class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if len(board) != 9:
            return False

        rowDuplicate = {}
        colDuplicate = {}

        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if board[i][j] != ".":
                    if i in rowDuplicate and board[i][j] in rowDuplicate[i]:
                        return False
                    #REGLE 1
                    if i in rowDuplicate and board[i][j] not in rowDuplicate[i]:   
                        rowDuplicate[i].append(board[i][j]) 
                    else:
                        rowDuplicate[i] = [board[i][j]]
                    
                    #REGLE 2
                    if j in colDuplicate and board[i][j] in colDuplicate[j]:
                        
                        return False
                    
                    if j in colDuplicate and board[i][j] not in colDuplicate[j]:   
                        colDuplicate[j].append(board[i][j]) 
                    else:
                        colDuplicate[j] = [board[i][j]] 
                
        # Regle 3 
        
        for ligne in range(0,len(board),3):
            
            for colonne in range(0,len(board),3):
                sousEspace = set()
                for i in range(ligne,ligne+3):
                    for j in range(colonne,colonne+3):
                        if board[i][j] != ".":
                            val = board[i][j]
                            if val in sousEspace:
                                
                                return False
                            sousEspace.add(val)


        return True
                               
