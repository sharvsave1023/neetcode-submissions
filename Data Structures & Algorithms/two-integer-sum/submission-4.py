class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # nums element : index

        for i, n in enumerate(nums):
            diff = target - n # target - current n
            if diff in m.keys(): # if diff in keys of m
                return [m[diff], i] # return that index, curr i
            else:
                m[n] = i # add that n, and index to dict