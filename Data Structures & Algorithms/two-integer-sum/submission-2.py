#BRUTE FORCE APPROACH
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map1 = {}
        for i in range(len(nums)):
            
            difference = target - nums[i]

            if difference in map1:
                return [map1[difference], i]
            
            map1[nums[i]] = i

        return []
                




