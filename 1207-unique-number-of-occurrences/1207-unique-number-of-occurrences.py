class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # occurence = {}
        # occ_set = set()
        # for i in arr:
        #     occurence[i] = occurence.get(i, 0) + 1
        # for i in occurence.values():
        #     if i in occ_set:
        #         return False
        #     occ_set.add(i)
        # return True
        occ = defaultdict(int)
        for i in arr:
            occ[i] += 1
        s = set()
        for c in occ.values():
            s.add(c)
        return len(s) == len(occ) 