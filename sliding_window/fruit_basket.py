def fruit_into_baskets(fruits):
  state = {} # choose appropriate data structure
  start = 0
  max_ = 0

  for end in range(len(fruits)):
    # extend window
    # add nums[end] to state in O(1) in time
    state[fruits[end]] = state.get(state[end] , 0) +1

    while state > 2:
      # repeatedly contract window until it is valid again
      # remove nums[start] from state in O(1) in time
        state[start] -= 1
        if state[start]==0:
            del state[start]

        start += 1

    # INVARIANT: state of current window is valid here.
    max_ = max(max_, end - start + 1)

  return max_

#Write a function to calculate the maximum number 
# of fruits you can collect from an integer array fruits, 
# where each element represents a type of fruit. You can start collecting 
# fruits from any position in the array, but you must stop once you 
# encounter a third distinct type of fruit. The goal is to find the longest 
# subarray where at most two different types of fruits are collected.
