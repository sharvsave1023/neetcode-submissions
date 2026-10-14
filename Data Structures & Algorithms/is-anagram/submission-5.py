class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False 

        n = len(s)
        s_count = [0 for _ in range(26)]
        t_count = [0 for _ in range(26)]

        for i in range(n): 

            s_count[ord(s[i]) - ord("a")] += 1
            t_count[ord(t[i]) - ord("a")] += 1

        return s_count == t_count