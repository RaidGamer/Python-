def mkMatrix(r, c):
    if isinstance(r, int) and isinstance(c, int):
        matrix = []
        for i in range(r+1):
            row = [j for j in range(c+1)]
            matrix.append(row)
        return matrix
    else:
        return -1
    

def printMatrix(m):
        xy = dim(m)
        if xy != -1:
            for i in range(xy[0]):
                for j in range(xy[1]):
                    print(m[i][j], end=' ')
                print()
                
def dim(m):
    if isinstance(m, list) and all(isinstance(row, list) for row in m):
        if isMatrix(m) != -1:
            return (len(m), len(m[0]))
    return -1

def isMatrix(m):
    if not (isinstance(m, list) and all(isinstance(row, list) for row in m)):
        return -1
    row_length = len(m[0])
    for row in m:
        if len(row) != row_length:
            return -1
    return 1
            
    
    



            

def main():
    matrix = mkMatrix(8,8)
    printMatrix(matrix)
    print(matrix)

main()