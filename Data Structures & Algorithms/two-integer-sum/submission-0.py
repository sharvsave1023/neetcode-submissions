class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         prevMap = {}

         for index, number in enumerate(nums):
            difference = target - number

            if difference in prevMap:
                return [prevMap[difference], index]
            prevMap[number] = index