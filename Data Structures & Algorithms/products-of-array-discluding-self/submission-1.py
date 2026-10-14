class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initial values of 1
        result = [1] * len(nums)
        #prefix defaults to 1
        prefix = 1
        #each res value is equal to prefix in each pass
        #prefix becomes product of itself and nums element
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        #postfix defaults to 1
        #each res value is equal to product of postfix and prefix
        #postfix becomes product of itself and nums element
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result