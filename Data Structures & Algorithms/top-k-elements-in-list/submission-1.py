import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        heap = []
        for val, freq in counter.items():
            heap.append((-freq, val))
        heapq.heapify(heap)
        
        res = []
        for i in range(0, k):
            res.append(heapq.heappop(heap)[1])
        return res
        