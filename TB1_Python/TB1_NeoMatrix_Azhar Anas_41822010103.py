import re

def process_matrix_file(file_path):
    print("\nMatrix Script:\n")

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    rows, cols = map(int, lines[0].split())

    matrix = [list(line.strip()) for line in lines[1:]]
    matrix = [row + [" "] * (cols - len(row)) for row in matrix]

    trans_matrix = list(zip(*matrix))

    decode = "".join("".join(row) for row in trans_matrix)
    print("\nAfter Decode:", decode)

    add_space = ""
    for row in trans_matrix:
        add_space += " ".join(re.findall(r'[a-zA-Z]+', "".join(row))) + " "
    print("Adding Space:", add_space)

process_matrix_file("matrix1.txt")