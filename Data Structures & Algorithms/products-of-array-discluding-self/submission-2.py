class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums: [1,2,3,4]
        pref array: [1, 2, 6, 24] 
            every value at pref[i] is nums[i] * pref[i-1]
        suff array: [24, 24, 12, 4]
            every value at suff[i] is nums[i] * suff[i+1]
        res: [24, 12, 8, 6]
            every value at res[i] is pref[i-1] * suff[i+1]
        '''

        n = len(nums)
        res = [0]*n
        pref = [0]*n
        suff = [0]*n

        pref[0] = 1
        suff[n-1] = 1

        # pref pass, start @ 1 to skip pref[0]
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        # suff pass, start @ n-2 to skip suff[n-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        # res pass
        for i in range(0, n):
            res[i] = pref[i] * suff[i]

        return res


