# from typing import List 


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         #return the total water
#         #area = x-1 * smallest y
#         #I would use max here to the value and keep moving
#         max_water = 0

#         l = 0
#         r = len(height)-1
#         while l < r:
#             min_height = min(height[l], height[r])
#             area = (r-l) * min_height
#             max_water = max(max_water, area)
#             if height[l]< height[r]:
#                 l+=1

#             else:
#                 r+=1
#         return max_water




from typing import List


def container_with_most_water(self, height: List[int]) -> int:
    l=0
    r=len(height)-1
    total = 0

    while l < r:
        min_h = min(height[l], height[r])
        area = min_h * (r-l)
        total = max(total, area)
        if height[l] < height[r]:
            l+=1
        else: 
            r -=1

    return total





def test_container_with_most_water():
    # Test case 1: Standard example
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected_output = 49 
    result = container_with_most_water(height)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test case 2: All heights are the same
    height = [5, 5, 5, 5]
    expected_output = 16
    result = container_with_most_water(height)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test case 3: Single element list (should return 0 as no two lines can form a container)
    height = [5]
    expected_output = 0
    result = container_with_most_water(height)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test case 4: Two elements list (should return the area of the single container formed by both lines)
    height = [2, 1]
    expected_output = 1
    result = container_with_most_water(height)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test case 5: Already sorted in descending order (should return the area of the first two lines)
    height = [8, 7, 6, 5, 4, 3, 2, 1]
    expected_output = 7
    result = container_with_most_water(height)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test case 6: Random heights with some higher and lower values
    height = [4, 3, 2, 1, 4, 2, 1]
    expected_output = 8
    result = container_with_most_water(height)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    print("All tests passed!")

# Call the test function to run all the tests
test_container_with_most_water()
