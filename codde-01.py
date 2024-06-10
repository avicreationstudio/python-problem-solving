input_value = list(map(int,input().split()))
rc = input_value[0]
cc = input_value[1]

matrix = []
for i in range(rc):
    row = list(map(int,input().split()))
    matrix.append(row)

print(matrix)