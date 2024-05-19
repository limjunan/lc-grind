class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width, height = len(matrix[0]), len(matrix)
        output = []
        heightStart, heightEnd, widthStart, widthEnd = 0, height, 0, width
        area = (width) * (height)

        while len(output) <= area:
            #print(output, 0)
            for w in range(widthStart, widthEnd):
                output.append(matrix[heightStart][w])
            if len(output) == area: break
            heightStart += 1
            #print(output, 1)

            for i in range(heightStart, heightEnd):
                output.append(matrix[i][widthEnd - 1])
            if len(output) == area: break
            widthEnd -= 1
            #print(output, 2)

            for w in reversed(range(widthStart, widthEnd)):
                output.append(matrix[heightEnd - 1][w])
            #print(output, 3)
            if len(output) == area: break
            heightEnd -=1

            for i in reversed(range(heightStart, heightEnd)):
                output.append(matrix[i][widthStart])
            #print(output, 4)
            if len(output) == area: break
            widthStart += 1
            

        return output
