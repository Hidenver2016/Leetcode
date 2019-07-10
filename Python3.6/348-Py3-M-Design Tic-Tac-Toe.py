# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:48:48 2019

@author: hjiang
"""

"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, 
or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
https://leetcode.com/problems/design-tic-tac-toe/discuss/81932/Python-13-lines-easy-to-understand
Record the number of moves for each rows, columns, and two diagonals.
For each move, we -1 for each player 1's move and +1 for player 2's move.
Then we just need to check whether any of the recored numbers equal to n or -n.
"""

class TicTacToe(object):

    def __init__(self, n):
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n
        
    def move(self, row, col, player):
        offset = player * 2 - 3#For each move, we -1 for each player 1's move and +1 for player 2's move. 这种操作考试是肯定想不出的
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0
    
    
"""
Essentially they're magic numbers:
0 == row win
1 == column win
2 == diagonal
3 == anti-diagonal

So: that type of win (row, column, diag, anti-diag), for that row/column/etc, for that player, is incremented by 1.
https://leetcode.com/problems/design-tic-tac-toe/discuss/81896/78-lines-O(1)-JavaPython

每次走一颗子，就把这个子在四个坐标上的位置全部标出，等到哪个位置为n，自然就赢了
因为如果对手打断，那么这个位置自然不会有子再增加
"""
import collections    
class TicTacToe(object):#看这个把
    def __init__(self, n):
        count = collections.Counter()
        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):# i是0，1，2，3； x是row, col, row+col, row-col
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move










