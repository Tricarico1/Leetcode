# Problem Statement:
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to the target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twosum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        com = target - num
        if com in dic:
            return i, dic[com] 
        else:
            dic[num]=i
    return None

nums = [2, 7, 11, 15]
target = 9
print(twosum(nums, target))  # Output: [0, 1]
            