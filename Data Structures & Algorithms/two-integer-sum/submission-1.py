class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dat = {} #val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dat:
                return [dat[diff], i]
            dat[n] = i
        return