#brainfuck_code = """
#++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
#"""

operators = ['<', '>', '+', '-', '[', ']', '.', ',']
brainfuck_code = []

with open("brainfuck.bf") as file:
  lines = file.readlines()
  for line in lines:
    for char in line:
        if char in operators:
            brainfuck_code += char
        else:
            print(f'greska')
            exit(1)

python_code = []
python_code.append("a = [0]*30000\n")
python_code.append("ptr = 0\n")
tab = 0

def bf_transp():
    global python_code
    global tab
    for char in brainfuck_code:
        if char == ',':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append('a[ptr] = ord(input())\n')
        elif char == '.':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append("print(chr(a[ptr]), end='')\n") 
        elif char == '+':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append("a[ptr]+=1\n") 
        elif char == '-':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append("a[ptr]-=1\n") 
        elif char == '<':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append("ptr-=1\n")
        elif char == '>':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append("ptr+=1\n")
        elif char == '[':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append('while(True):\n')
            tab += 1
        elif char == ']':
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append('if(a[ptr] == 0):\n')
            for i in range(0,tab):
                python_code.append('\t')
            python_code.append('\tbreak\n')
            tab -= 1


bf_transp()
file1 = open("./python_code.py", "w")

for command in python_code:
    file1.write(command)

file1.close()

#petlje
#potencijalna provera gresaka