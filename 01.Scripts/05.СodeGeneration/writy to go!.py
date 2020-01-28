import numpy as np


def my_reshape(array, line, column):
    result = np.empty((line, column))
    if line == 1:
        i = 0
        for j in range(column):
            result[i][j] = array[j][i]
    elif column == 1:
        j = 0
        for i in range(line):
            result[i][j] = array[i]
    else:
        o_col = np.shape(A)[1] - 1
        i = 0
        j = 0

        for n_line in range(line):
            for n_col in range(column):
                result[n_line][n_col] = array[i][j]
                j += 1

                if j > o_col:
                    j = 0
                    i += 1
    return result


A = np.array([[0, 1, 2],
             [3, 4, 5]])

print(A.ravel())
