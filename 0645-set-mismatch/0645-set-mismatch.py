class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = -1
        m = -1
        for i in range(1, len(nums)+1):
            c = nums.count(i)
            if c == 2:
                d = i
            elif c == 0:
                m = i
        return [d, m]

