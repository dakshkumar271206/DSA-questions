class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        max_width = numRows * 4 
        for row in triangle:
            row_string = "   ".join(map(str, row))
            print(row_string.center(max_width))
        return triangle