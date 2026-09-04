class Solution {
    public void solveSudoku(char[][] board) {
        solver(board, 0, 0);
    }
    private boolean solver(char[][] board, int row, int col){
        if(row == 9){
            return true;
        }

        int nextRow = row;
        int nextCol = col + 1;
        if(nextCol == 9){
            nextRow = row + 1;
            nextCol = 0;
        }

        if(board[row][col] != '.'){
            return solver(board, nextRow, nextCol);
        }

        for(char i = 1; i <= 9; i++){
            if(safe(board, row, col, i)){
                board[row][col] = (char) ('0' + i);

                if(solver(board, nextRow, nextCol)){
                    return true;
                }

                board[row][col] = '.';
            }
        }
        return false;
    }

    private boolean safe(char[][] board, int row, int col, int val){
        for(int i = 0; i < 9; i++){
            if(board[row][i] == (char) ('0' + val)){
                return false;
            }
        }

        for(int i = 0; i < 9; i++){
            if(board[i][col] == (char) ('0' + val)){
                return false;
            }
        }

        int sr = (row / 3) * 3;
        int sc = (col / 3) * 3;

        for(int i = sr; i < sr + 3; i++){
            for(int j = sc; j < sc + 3; j++){
                if(board[i][j] == (char) ('0' + val)){
                    return false;
                }
            }
        }

        return true;
    }
}