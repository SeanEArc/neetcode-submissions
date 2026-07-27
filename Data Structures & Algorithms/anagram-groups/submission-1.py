class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs];

        strmap = {}

        for i in range(len(strs)):
            current = strs[i]
            
            sorted_word = "".join(sorted(current))

            if sorted_word in strmap:
                strmap[sorted_word].append(current)
                
            else:
                strmap[sorted_word] = [current]


        return list(strmap.values());
        