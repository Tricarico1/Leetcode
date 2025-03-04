from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        left_h = height[l]
        right_h = height[r]
        total = 0

        while l+1 < r:
            if left_h < right_h:
                l +=1
                if height[l] < left_h:
                    total += left_h - height[l]
                left_h = height[l]

            else:
                r-=1
                if height[r] < right_h:
                    total += right_h - height[r]
                right_h = height[r]
        return total