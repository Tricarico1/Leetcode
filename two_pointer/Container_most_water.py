from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #return the total water
        #area = x-1 * smallest y
        #I would use max here to the value and keep moving
        max_water = 0

        l = 0
        r = len(height)-1
        while l < r:
            min_height = min(height[l], height[r])
            area = (r-l) * min_height
            max_water = max(max_water, area)
            if height[l]< height[r]:
                l+=1

            else:
                r+=1
        return max_water



