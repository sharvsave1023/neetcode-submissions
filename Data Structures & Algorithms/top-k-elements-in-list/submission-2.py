import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # val : freq
        for i in range(0, len(nums)):
            if nums[i] in count.keys():
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        sort = sorted(count.items(), key = lambda item: item[1], reverse = True)

        res = []
        for i in range(0, k):
            val = sort[i][0]
            res.append(val)

        return res