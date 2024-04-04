class Solution:
    def twoSum(self, nums, target):

        adds = {}

        for x, num in enumerate(nums):
            add = target - num

            if add in adds:
                return [adds[add], x]

            adds[num] = x

        return[]

target = 12
nums = [1, 3, 9, 11]

result = Solution().twoSum(nums, target)
print(result)