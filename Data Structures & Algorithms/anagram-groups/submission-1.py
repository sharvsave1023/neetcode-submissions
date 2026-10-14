class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        # counts : list of strings (words)
        elements = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s: # one indv. string
                counts[ord(c) - ord('a')] += 1
                
            elements[tuple(counts)].append(s)
        
        for val in elements.values():
            res.append(val)

        return res

        

