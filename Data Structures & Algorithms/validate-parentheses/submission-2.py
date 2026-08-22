class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False

        print(s)

        stack = []

        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack.pop() != valid[ch]:
                    return False
            

        

        return len(stack) == 0