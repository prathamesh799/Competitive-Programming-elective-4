# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    # condition for matrix multiplication
    # m1 cols = m2 rows
    if len(m1[0]) !=  len(m2):
        return None
    res = [[i for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            print([k for k in range(len(m1[0]))])
            res[i][j] = sum([m1[i][k] * m2[k][j] for k in range(len(m1[0]))])
    return res

print(fun_matrixmultiply([[1,3],[2,4]],  [[1,3,2,2], [2,4,5,1]]))
