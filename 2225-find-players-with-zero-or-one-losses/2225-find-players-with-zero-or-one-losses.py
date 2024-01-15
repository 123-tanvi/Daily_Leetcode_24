class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        looser = defaultdict(int)
        for i in matches:
            winner[i[0]] += 1
            looser[i[1]] += 1
        res = [[],[]]
        for key, value in winner.items():
            if key not in looser:
                res[0].append(key)
        for key, value in looser.items():
            if value == 1:
                res[1].append(key)
        res[0] = sorted(res[0])
        res[1] = sorted(res[1])
        return res
        