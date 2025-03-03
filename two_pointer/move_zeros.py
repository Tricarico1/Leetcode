from typing import List


#code 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
                nextNonZero += 1

                            

#Code 2

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)

        while l<r:
            if nums[l] ==0:
                nums.append(0)
                nums.remove(nums[l])
                l+=1
            else:
                l+=1

            

        return nums
        