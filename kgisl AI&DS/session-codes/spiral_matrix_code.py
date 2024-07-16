import prettytable

def generate_spiral(n):
    if n <= 0:
        return [], []  # Return empty lists for non-positive n

    m = [["_" for j in range(n)] for i in range(n)]
    chakra = [["_" for j in range(n)] for i in range(n)]

    left = 0
    right = n - 1
    top = 0
    bottom = n - 1

    counter = 1

    while left <= right and top <= bottom:
        # left - right
        for j in range(left, right + 1):
            m[top][j] = counter
            chakra[top][j] = '\\' if j == right else '-'
            counter += 1
        top += 1

        # top - bottom
        for i in range(top, bottom + 1):
            m[i][right] = counter
            chakra[i][right] = '/' if i == bottom else '|'
            counter += 1
        right -= 1

        if top <= bottom:  # Check if there are remaining rows
            # right - left
            for j in range(right, left - 1, -1):
                m[bottom][j] = counter
                chakra[bottom][j] = '\\' if j == left else '-'
                counter += 1
            bottom -= 1

        if left <= right:  # Check if there are remaining columns
            # bottom - top
            for i in range(bottom, top - 1, -1):
                m[i][left] = counter
                chakra[i][left] = '/' if i == top else '|'
                counter += 1
            left += 1

    return m, chakra

n = 5  # Change this value to test different sizes
matrix, chakra = generate_spiral(n)

p = prettytable.PrettyTable()

for row in matrix:
    p.add_row(row)

print(p)

for row in chakra:
    print(*row, sep=" ")
