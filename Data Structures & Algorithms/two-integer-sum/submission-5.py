class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        dicti = {}

        for i in range(len(nums)):
            
            difference = target - nums[i]

            if difference in dicti:
                return [dicti[difference], i]
            
            dicti[nums[i]] = i




