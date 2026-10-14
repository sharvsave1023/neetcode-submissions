class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # array of 1's the size of n
        res = [1] * len(nums) # [1, 1, ..., 1]
        'example nums = [1, 2, 3, 4]'
        # nums fwd pass
        prefix = 1
        for i in range(len(nums)):
            # res[i] is prefix
            res[i] = prefix
            # update prefix to be product of the values before
            prefix *= nums[i]
        'after fwd pass: res = [1, 1, 2, 6]'
        # each res[i] holds the product of all to its left:

        # nums bwd pass
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            # res[i] times values after it
            res[i] *= postfix
            # update postfix to be product of values after it
            postfix *= nums[i]
        'after bwd pass: res = [24, 12, 8, 6]'
        # bwd pass: mult. each res[i] by the product of all to its right:

        return res
