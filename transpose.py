def transpose(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for _ in range(cols):
        result.append([0] * rows)

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result
