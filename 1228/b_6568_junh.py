
memory = ['11111111' for _ in range(32)]
calc = '0'*8
pc = '0'*5

def STA(val):
    val = int(val, 2)
    memory[val] = calc

def LDA(val):
    global calc
    val = int(val, 2)
    calc = memory[val]

def BEQ(val):
    global pc
    if not int(calc):
        pc = val

def NOP():
    pass

def DEC():
    global calc
    tmp = int(calc, 2)-1
    tmp = bin(tmp)[2:]
    if len(tmp)>8:
        tmp = tmp[-8:]
    calc = '0'*(8-len(tmp)) + tmp

def INC():
    global calc
    tmp = int(calc, 2)+1
    tmp = bin(tmp)[2:]
    if len(tmp)>8:
        tmp = tmp[-8:]
    calc = '0'*(8-len(tmp)) + tmp

def JMP(val):
    global pc
    pc = val

def HLT():
    global calc, pc
    print(calc)
    calc = '0'*8
    pc = '0'*5

def com_start():
    global pc
    tmp = int(pc, 2) + 1
    tmp = bin(tmp)[2:]
    if len(tmp)>5:
        tmp = tmp[-5:]
    pc = '0' * (5 - len(tmp)) + tmp


for _ in range(32):
    inp = input()
    com = inp[:3]
    val = inp[3:]

    com_start()
    if com == '000':
        STA(val)
    elif com == '001':
        LDA(val)
    elif com == '010':
        BEQ(val)
    elif com == '011':
        NOP()
    elif com == '100':
        DEC()
    elif com == '101':
        INC()
    elif com == '110':
        JMP(val)
    elif com == '111':
        HLT()