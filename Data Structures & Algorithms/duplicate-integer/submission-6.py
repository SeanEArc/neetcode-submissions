class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dicti = {}

        for i in range(len(nums)):
            if nums[i] not in dicti:
                dicti[nums[i]] = 0
            else:
                return True


        return False
            
            