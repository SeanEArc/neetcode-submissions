class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dummy_dict = {}
        dummy_array = []

        for i in range(len(nums)):
            dummy_dict[nums[i]] = dummy_dict.get(nums[i], 0) + 1
            print(dummy_dict)

        for i in range(k):
            highest = max(dummy_dict, key=dummy_dict.get)
            dummy_array.append(highest)
            dummy_dict.pop(highest)

            print(highest)



        return dummy_array
        