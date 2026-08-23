class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                previousIndex = stack.pop()

                result[previousIndex] = i - previousIndex


            stack.append(i)

        return result
        