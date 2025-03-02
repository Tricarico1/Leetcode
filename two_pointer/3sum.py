from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        final = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l=i+1
            r=len(nums)-1

            while l < r:
                rem = nums[l] + nums[r] + nums [i]
                if rem == 0:
                    final.append([nums[l],nums[r], nums[i]])
                    while l < r and nums[l]==nums[l+1]:
                        l+=1
                    while l < r and nums[r]==nums[r-1]:
                        r-=1
                elif rem > 0:
                    l +=1
                    continue
                else:
                    r -=1
                    continue

        return final
