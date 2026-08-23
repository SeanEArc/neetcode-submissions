class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operators = ('+','-','*','/')

        for i in range(len(tokens)):

            if tokens[i] in operators:
                right = stack.pop()
                left = stack.pop()
                currentOp = tokens[i]

                if currentOp == '+':
                    stack.append(right + left)
                elif currentOp == '-':
                    stack.append(left - right)
                elif currentOp == '*':
                    stack.append(left * right)
                elif currentOp == '/':
                    stack.append(int(left / right))
            
            else:
                stack.append(int(tokens[i]))

            
        print(stack)
        return stack[0]