import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

def STA(val):
    memory[val] = calc

def LDA(val):
    global calc
    calc = memory[val]

def BEQ(val):
    global pc
    if not calc:
        pc = val

def NOP():
    pass

def DEC():
    global calc
    calc = (calc-1) % 256

def INC():
    global calc
    calc = (calc+1) % 256

def JMP(val):
    global pc
    pc = val

def HLT():
    pass

def com_start():
    global pc
    pc = (pc + 1) % 32


while True:
    memory = [0 for _ in range(32)]
    for i in range(32):
        try:
            memory[i] = int(input().rstrip(), 2)
        except:                 # EOFError 말고 전체 Error로
            sys.exit()
    calc = 0
    pc = 0

    while True:
        inp = memory[pc]
        com = inp//32
        val = inp%32
        com_start()

        if com == 0:
            STA(val)
        elif com == 1:
            LDA(val)
        elif com == 2:
            BEQ(val)
        elif com == 3:
            NOP()
        elif com == 4:
            DEC()
        elif com == 5:
            INC()
        elif com == 6:
            JMP(val)
        elif com == 7:
            HLT()
            break

    print(bin(calc)[2:].zfill(8))