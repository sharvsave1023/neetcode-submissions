class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n # target - current n
            if diff in m.keys():
                return [m[diff], i]
            else:
                m[n] = i            