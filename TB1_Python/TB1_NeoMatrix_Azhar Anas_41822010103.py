import re

print("\nMatrix Script:\n")
def read_matrixfile(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    rows, cols = map(int, lines[0].split())

    matrix = [list(line.strip()) for line in lines[1:]]
    matrix = [row + [" "] * (cols - len(row)) for row in matrix]
    
    return matrix

matrix = read_matrixfile("matrix1.txt")
trans_matrix = list(zip(*matrix))

decode = "".join("".join(row) for row in trans_matrix)
print("\nAfter Decode:", decode)

add_space = re.sub(r"(?<=\w)([^\w\d]+)(?=\w)", " ", decode)
print("Adding Space:", add_space)