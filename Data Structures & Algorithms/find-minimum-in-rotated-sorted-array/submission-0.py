class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0

        right = len(nums) - 1



        while left < right:

            middle = (left + right) // 2

            if nums[middle] > nums[right]:

                left = middle + 1
                print(left)
            
            else:

                right = middle
                print(right)


        return nums[left]

            

        