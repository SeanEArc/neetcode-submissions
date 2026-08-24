class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:

            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            
            elif target > matrix[row][-1]:
                top = row + 1
            
            else:
                left = 0
                right = len(matrix[row]) - 1

                while left <= right:

                    middle = (left + right) // 2

                    if matrix[row][middle] == target:
                        return True
                    elif matrix[row][middle] < target:
                        left = middle + 1
                    elif matrix[row][middle] > target:
                        right = middle - 1
            
                break
            
            
                


        return False



                

            

