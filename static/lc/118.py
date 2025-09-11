class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # numRow constraints
        # 1 <= numRows <= 30

        res = [[0 for _ in range(i + 1)] for i in range(numRows)]
        res[0][0] = 1
        for i in range(1, numRows):
            for j in range(len(res[i])):
                # OOB check
                left = res[i - 1][j - 1] if j - 1 >= 0 else 0
                above = res[i - 1][j] if j < len(res[i - 1]) else 0
                res[i][j] = left + above
        return res