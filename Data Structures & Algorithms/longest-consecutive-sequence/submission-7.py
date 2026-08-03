class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0;

        sorted_array = set(nums)
        actual_array = list(sorted(sorted_array))
        con = 1
        max = 1

        for i in range(len(actual_array) - 1):
            if actual_array[i + 1] - actual_array[i] == 1:
                con = con + 1
                if con > max:
                    max = con
            else:
                con = 1


        return max;
        