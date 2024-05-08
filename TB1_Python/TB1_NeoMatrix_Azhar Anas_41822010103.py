import re

def matrix_input():
    return [tuple(row) for row in iter(input, "")]

print("\nMatrix Script:\n")
trans_matrix = list(zip(*matrix_input()))

decode = "".join("".join(row) for row in trans_matrix)
print("After Decode:", decode)

add_space = ""
for row in trans_matrix:
    add_space += " ".join(re.findall(r'[a-zA-Z]+', "".join(row))) + ""
print("Adding Space:", add_space)


"""

Matrix Script Example:

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

"""