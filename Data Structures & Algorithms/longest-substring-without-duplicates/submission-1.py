class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        left = 0
        right = 0

        longest = 0
        my_set = set()

        while right < len(s):

            if s[right] not in my_set:
                my_set.add(s[right])
                right += 1
                
                if len(my_set) > longest:
                    longest = len(my_set)
        
            else:
                my_set.remove(s[left])
                left += 1
                

        return longest

            

            
