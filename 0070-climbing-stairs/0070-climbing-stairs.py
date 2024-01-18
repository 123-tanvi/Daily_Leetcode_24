class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # if n>=3:
        #     return (n-1) + (n-2)
        p1 = 1
        p2 = 2
        res = 0
        for i in range(2, n):
            res = p1+p2
            p1 = p2
            p2 = res
        return res