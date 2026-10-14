class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # look for min as well as max, multiply later number
            # with running product 
        # all positive, product increases
        # all negative, alternates +ve and -ve products

        # edge case of 0?
        # 0 kills the streak
        # anytime we see a 0, set max and min to 1, so that we don't
            # include 0 at all in the product, and we multiply the next
            # item such that it just becomes itself by either min or max

        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            # max could be the element times max, min, or be just itself
            # store tmp because currMax gets recomputed
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax)

        return res