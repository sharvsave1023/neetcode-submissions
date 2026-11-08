class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2

        # count val, freq in nums
        counter = {}
        for n in nums:
            if n in counter.keys():
                counter[n] += 1
            else:
                counter[n] = 1
        
        # val: freq
        # sort by the frequency

        sorted_array = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_array[i][0])

        return res



        

        

        