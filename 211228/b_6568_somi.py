def STA(x):
    memory[x] = calc

def LDA(x):
    global calc
    calc = memory[x]

def BEQ(x):
    global pc
    if calc == 0:
        pc = x

def DEC(x):
    global calc
    calc -= 1

def INC(x):
    global calc
    calc += 1

def JMP(x):
    global pc
    pc = x


memory = [0] * 32
pc = 0
calc = 0
for _ in range(32):
