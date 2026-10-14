class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in diffs.keys():
                return [diffs[difference], i]
            diffs[n] = i