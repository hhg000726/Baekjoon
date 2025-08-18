import sys

N, B = map(int, sys.stdin.readline().split())

ori_matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    ori_matrix.append(row)

def matrix_mult(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]
    
    for i in range(n):
        for j in range(m):
            result[i][j] %= 1000
    
    return result

matrixs = [ori_matrix]
for i in range(40):
    matrixs.append(matrix_mult(matrixs[-1], matrixs[-1]))

binary = bin(B)[2:][::-1]
result_matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for i in range(len(binary)):
    if binary[i] == '1':
        result_matrix = matrix_mult(result_matrix, matrixs[i])

for row in result_matrix:
    print(' '.join(map(str, row)))
