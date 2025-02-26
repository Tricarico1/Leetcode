# Problem Statement: Given a 1-indexed array nums of distinct integers, and an integer target, 
# find the two numbers such that they add up to the target.

def sumII(nums, target):
    l = 0
    r = len(nums)-1

    while l < r:
        sum = nums[r] + nums[l]
        if sum == target:
            return (nums[r],  nums[l])
        elif (sum) < 0:
            l += 1
        else:
            r -= 1


    return None

nums = [2, 7, 11, 15]
target = 9
print(sumII(nums, target))  # Output: [1, 2]