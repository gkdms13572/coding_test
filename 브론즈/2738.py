# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

n, m = map(int,input().split())
A = []
B = []

for _ in range(n):
    row = list(map(int,input().split()))
    A.append(row)

for _ in range(m):
    row = list(map(int,input().split()))
    B.append(row)

for row in range(n):
    for col in range(m):
        print(A[row][col] + B[row][col],end=' ')
    print()
