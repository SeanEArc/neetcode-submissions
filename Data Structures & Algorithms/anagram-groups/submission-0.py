class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs];

        strmap = {}

        #Iterate through input array
        for i in range(len(strs)):
            print(strs[i])
            current = strs[i]
            
            sorted_word = "".join(sorted(current))
            print(sorted_word)

            if sorted_word in strmap:
                strmap[sorted_word].append(current)
                

            else:
                strmap[sorted_word] = [current]


        print(strmap)
        print(list(strmap.values()))



        #return dummy
        return list(strmap.values());
        