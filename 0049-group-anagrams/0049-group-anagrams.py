class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        d = {}
        for w in words:
            key = "".join(sorted(w))
            if key not in d:
                d[key] = [w]
            else:
                d[key].append(w)
        return d.values()