class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initial values of 1
        result = [1] * len(nums)

        #prefixes
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result