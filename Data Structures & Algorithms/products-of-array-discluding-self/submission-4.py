class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # array of 1's the size of n
        res = [1] * len(nums) # [1, 1, ..., 1]
        
        # nums fwd pass
        prefix = 1
        for i in range(len(nums)):
            # res[i] is prefix
            res[i] = prefix
            # update prefix to be product of the values before
            prefix *= nums[i]

        # nums bwd pass
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            # res[i] times values after it
            res[i] *= postfix
            # update postfix to be product of values after it
            postfix *= nums[i]

        return res
