class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dicts = {}
        dictt = {}

        for i in range(len(s)):
            
            currents = s[i]
            currentt = t[i]


            if currents in dicts:
                dicts[currents] += 1
            else:
                dicts[currents] = 0

            if currentt in dictt:
                dictt[currentt] += 1
            else:
                dictt[currentt] = 0


        if dicts == dictt:
            return True

        return False