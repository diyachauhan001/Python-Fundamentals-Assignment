# Split Array Largest Sum


def splitArray( nums, k):
    l = max(nums)
    r = sum(nums) + 1

    def numGroups(maxSumInGroup):
      groupCount = 1
      sumInGroup = 0

      for num in nums:
        if sumInGroup + num <= maxSumInGroup:
          sumInGroup += num
        else:
          groupCount += 1
          sumInGroup = num

      return groupCount

    while l < r:
      m = (l + r) // 2
      if numGroups(m) > k:
        l = m + 1
      else:
        r = m

    return l

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))
