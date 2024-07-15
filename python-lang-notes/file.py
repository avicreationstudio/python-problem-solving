# # rc, cc = map(int,input().split())
# # matrix = []
# # for _ in range(rc):
# #     row = list(map(int,input().split()))
# #     matrix.append(row)
# matrix = [
#     [ 1, 2, 3, 4, 5],
#     [18,19,20,21, 6],
#     [17,28,29,22, 7],
#     [16,27,30,23, 8],
#     [15,26,25,24, 9],
#     [14,13,12,11,10],
# ]

# rc = len(matrix)
# cc = len(matrix[0])
# top = -1
# bottom = rc
# left = -1
# right = cc 

# while top < bottom and left < right:
#     for i in range(left+1,right):
#         print(matrix[top+1][i],end=" ")
#     top = top + 1

#     for i in range(top+1,bottom):
#         print(matrix[i][right-1],end=" ")
#     right = right - 1

#     for i in range(right-1,left,-1):
#         print(matrix[bottom-1][i],end=" ")
#     bottom = bottom - 1

#     for i in range(bottom-1, top,-1):
#         print(matrix[i][left+1],end=" ")
#     left = left + 1

import time 
eyes = "0-"
cat = r"""
  |\_|\
_/ {0} {0} |
| ^    | 
\_____./

"""
for i in range(100):
    time.sleep(0.5)
    print(cat.format(eyes[i%2]))
