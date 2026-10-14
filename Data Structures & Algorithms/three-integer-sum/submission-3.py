class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # a + b + c = 0
        # lead with the a

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue # if a+1 is the same as a, then skip
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r] #condition checker
                if threeSum > 0: # too high
                    r -= 1 # means answer must be lower
                elif threeSum < 0: # too low
                    l += 1 # means answer must be higher
                else:
                    res.append([a, nums[l], nums[r]]) # success
                    l += 1 # move to the next "b"
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 # if similar b's, then skip
        return res