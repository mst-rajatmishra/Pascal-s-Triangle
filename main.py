from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            # Start a new row
            row = [1] * (i + 1)
            
            # Fill in the values for the middle elements
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Append the row to the triangle
            triangle.append(row)
        
        return triangle

# Example usage:
sol = Solution()
print(sol.generate(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(sol.generate(1))  # Output: [[1]]
