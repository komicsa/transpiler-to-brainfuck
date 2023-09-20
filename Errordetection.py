

def proveraZagrade(brainfuck_kod):
    stack = []

    kod_je_ispravan = True

    for line in brainfuck_kod:
        for char in line:
            if char == '[':
                stack.append("[")
            elif char == ']':
                if len(stack) == 0:
                    print("Proverite sve zagrade")
                    kod_je_ispravan = False
                    return kod_je_ispravan
                stack.pop()

    is_empty = len(stack) == 0

    if is_empty == True:
        kod_je_ispravan = True
    else:
        kod_je_ispravan = False

    return kod_je_ispravan