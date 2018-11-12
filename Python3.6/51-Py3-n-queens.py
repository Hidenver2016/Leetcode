# Time:  O(n!)
# Space: O(n)
#
# The n-queens puzzle is the problem of placing n queens on 
# an nxn chess board such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# 
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
# 
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

# quick solution for checking if it is diagonally legal
class Solution:
    # @return an integer
    def solveNQueens(self, n):
        self.cols = [False] * n # 先全部置为假，这样子后面就可以用了,这个东西是对于每一列的指示，如果是true表示被皇后占据 （不关心行）
        self.main_diag = [False] * (2 * n) #主对角线row+i 会被占据
        self.anti_diag = [False] * (2 * n) # 次对角线用row-i+n, 我觉得这个n就是一个偏置，其实直接搞row-i也是对的
        self.solutions = [] #这个地方因为行不用考虑，一行只有一个皇后，所以依次排列的就是列的位置
        self.solveNQueensRecu([], 0, n)
        for ch in self.solutions: # 有几个解
            for sh in ch: # 解的每一行
                print (sh)                
            print ('\n')
        return len(self.solutions)
#        return self.solutions

    
    def solveNQueensRecu(self, solution, row, n):
        if row == n:
            self.solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution)) #这个地方就是一个输出格式
        else:
            for i in range(n): # 列遍历
                #这里实际上是剪枝， 看看能不能跑
                if not self.cols[i] and not self.main_diag[row + i] and not self.anti_diag[row - i + n]:
                    self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = True# 先置位
                    # 此处实现的row+1是对于行的遍历，把当前可行的答案附上（不一定以后也可行，因为下面一句是backtrack删除不行答案的）
                    self.solveNQueensRecu(solution + [i], row + 1, n)
                    # 删除不行的答案
                    self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = False

# slower solution
class Solution2:
    # @return an integer
    def solveNQueens(self, n):
        self.solutions = []
        self.solveNQueensRecu([], 0, n)
        return self.solutions
    
    def solveNQueensRecu(self, solution, row, n):
        if row == n:
            self.solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution))
        else:
            for i in range(n):
                if i not in solution and reduce(lambda acc, j: abs(row - j) != abs(i - solution[j]) and acc, range(len(solution)), True):
                    self.solveNQueensRecu(solution + [i], row + 1, n)

if __name__ == "__main__":
    results = Solution().solveNQueens(4)
    print (results)
    
    
    

