class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                print(True)
                return True
            
            map[nums[i]] = 1

        return False
