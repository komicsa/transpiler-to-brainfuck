operators = ['<', '>', '+', '-', '[', ']', '.', ',']
code = ''

with open("brainfuck.bf") as file:
  lines = file.readlines()
  for line in lines:
    for char in line:
        if char in operators:
            code += char

f = open('initOutput.txt', 'w')    
f.write(code)
f.close()