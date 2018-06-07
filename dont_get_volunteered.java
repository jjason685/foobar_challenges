public static int answer(int src, int dest) {
 int[][] board = new int[8][8];
 fillBoard(board, src, 0);
 return board[(int)(dest / 8)][(int)(dest % 8)];
}
public static void fillBoard(int[][] board, int currentPos, int numOfMoves) {
 int currentx = (int)(currentPos / 8);
 int currenty = (int)(currentPos % 8);

 int[] possibleRes = {
  1,
  2,
  2,
  1,
  2,
  -1,
  1,
  -2,
  -1,
  -2,
  -2,
  -1,
  -2,
  1,
  -1,
  2
 };
 for (int i = 0; i < 16; i += 2) {
  int newx = currentx + possibleRes[i];
  int newy = currenty + possibleRes[i + 1];
  if (newx >= 0 && newy >= 0 && newx < 8 && newy < 8) {
   if (board[newx][newy] == 0 || board[newx][newy] > numOfMoves + 1) {
    board[newx][newy] = numOfMoves + 1;
    fillBoard(board, newx * 8 + newy, numOfMoves + 1);
   }
  }
 }
}
