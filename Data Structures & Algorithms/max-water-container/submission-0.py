class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        # area defined as distance * min btwn. heights[l] or heights[r]
        while l < r:
            trial = min(heights[l], heights[r]) * (r - l)
            area = max(area, trial)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return area


