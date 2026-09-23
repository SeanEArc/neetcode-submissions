class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dicts = {}

        for i in range(len(nums)):

            if nums[i] in dicts:
                return nums[i]
            else:
                dicts[nums[i]] = 1
        