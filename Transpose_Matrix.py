class Solution(object):
    def transpose(self, matrix):
        cols, rows = len(matrix[0]),len(matrix)
        #arr = [[0]*rows]*cols
        arr = [[0] * rows for _ in range(cols)]  
        print(arr)
        for i in range(rows):
            for j in range(cols):
                arr[j][i]=matrix[i][j]

        return arr
        
