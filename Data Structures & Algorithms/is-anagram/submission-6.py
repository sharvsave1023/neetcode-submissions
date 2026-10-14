class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tChar, sChar = {}, {}
        for c in s:
            if c in sChar.keys():
                sChar[c] += 1
            else:
                sChar[c] = 1
        for c in t:
            if c in tChar.keys():
                tChar[c] += 1
            else:
                tChar[c] = 1
        return sChar == tChar

