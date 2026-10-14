class Solution:

    def find_max_count(self, d: dict) -> int:
        res = 0
        for val in d.values():
            res = max(res, val)
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = {}
        n = len(s)
        l = 0
        res = 0

        for r in range(n):
            if s[r] not in counts:
                counts[s[r]] = 0
            counts[s[r]] += 1
            
            total_count = r-l+1
            #while window invalid, incr left, decr window size
            while (r-l+1 - self.find_max_count(counts) > k):
                counts[s[l]] -= 1
                if counts[s[l]] == 0: 
                    del counts[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
        