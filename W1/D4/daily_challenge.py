# Challenge 1

import re

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''


matrix_lines = MATRIX_STR.strip().split('\n')
matrix = [list(row) for row in matrix_lines]

raw_message = ''
cols = len(matrix[0])
rows = len(matrix)

for col in range(cols):
    for row in range(rows):
        raw_message += matrix[row][col]


# \b[a-zA-Z]+(?:[^a-zA-Z]+[a-zA-Z]+)*\b will isolate word groups

decoded = re.sub(r'(?<=\w)([^a-zA-Z]+)(?=\w)', ' ', raw_message)


decoded = re.sub(r'^[^a-zA-Z]+', '', decoded)
decoded = re.sub(r'[^a-zA-Z]+$', '', decoded)

print(decoded)

