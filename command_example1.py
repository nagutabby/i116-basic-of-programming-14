from command import Command
from vm import *

push1 = Command(CName.PUSH, 1)
storeX = Command(CName.STORE, 'x')
storeY = Command(CName.STORE, 'y')
push5 = Command(CName.PUSH, 5)
lt = Command(CName.LT, None)
cjmp2 = Command(CName.CJMP, 2)
jmp10 = Command(CName.JMP, 10)
loadX = Command(CName.LOAD, 'x')
loadY = Command(CName.LOAD, 'y')
mul = Command(CName.MUL, None)
add = Command(CName.ADD, None)
jmpM13 = Command(CName.JMP, -13)
quit = Command(CName.QUIT, None)
cl = [push1, storeX, push1, storeY, loadY, push5, lt, cjmp2, jmp10, loadX, loadY, mul, storeX, loadY, push1, add, storeY, jmpM13, quit]
print(l2s(cl))
vm = VM(cl)
print(vm.run())
