class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        # char, occur.
        sMap, tMap = {}, {}
        #racecar, carrace
        for i in range(len(s)):
            # char's occur. = first occur + additional, 0 otherwise
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        return sMap == tMap

