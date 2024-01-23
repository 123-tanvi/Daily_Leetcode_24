class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        count = 0
        res = [""]
        for word in arr:
            for r in res:
                new_word = r + word
                if len(new_word) != len(set(new_word)):
                    continue
                res.append(new_word)
                count = max(count, len(new_word))
        return count