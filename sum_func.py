brainfuck_code = """
,
-
.
>>>>
<<
"""

mem_tape = [0] * 65536
pointer = 0

python_code = []

def brainfuck_input():
    global python_code
    for char in brainfuck_code:
        if char == ',':
            python_code.append("a = input()") #############jel tacno

def brainfuck_print():
    global python_code
    for char in brainfuck_code:
        if char == '.':
            python_code.append("print(a)") 


def pointers():
    global python_code
    pointer_right = 0
    pointer_left = 0
    for char in brainfuck_code:
        if char == '>':
            pointer_right += 1
        elif char == '<':
            pointer_left += 1

    print(pointer_right)
    print(pointer_left)

brainfuck_input()
brainfuck_print()
pointers()

python_code_str = "\n".join(python_code)
exec(python_code_str)

print(python_code_str)


