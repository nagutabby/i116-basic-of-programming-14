from stack import EmptyStack
from list_to_string import l2s
from custom_exception import VMError, DivisionByZeroException, UndefinedVariableException
from cname import CName

class VM():
    def __init__(self, cl) -> None:
        self.clist = cl
        self.stk = EmptyStack()
        self.environment: dict = {}
        self.pc = 0
    def str(self) -> str:
        return f'pc: {self.pc}, stack: {self.stk}, command list: {l2s(self.clist)}, environment: {self.environment}'

    def run(self):
        while True:
            if self.pc < 0 or self.pc >= len(self.clist):
                raise VMError('pc: ' + str(self.pc) + ' is out of scope of clist: ' + l2s(self.clist))
            com = self.clist[self.pc]
            if com.cname == CName.PUSH:
                self.stk = self.stk.push(com.num)
                self.pc = self.pc + 1
            elif com.cname == CName.MONE:
                if self.stk.is_empty():
                    raise VMError('stk is empty for mone')
                x = self.stk.top()
                self.stk = self.stk.pop().push(-1 * x)
                self.pc = self.pc + 1
            elif com.cname == CName.MUL:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for mul')
                y = self.stk.top()
                x = self.stk.pop().top()
                self.stk = self.stk.pop().pop().push(x * y)
                self.pc = self.pc + 1
            elif com.cname == CName.DIV:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for div')
                y = self.stk.top()
                x = self.stk.pop().top()
                if y == 0:
                    raise DivisionByZeroException('division by zero in VM')
                self.stk = self.stk.pop().pop().push(x / y)
                self.pc = self.pc + 1
            elif com.cname == CName.REM:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for rem')
                y = self.stk.top()
                x = self.stk.pop().top()
                if y == 0:
                    raise DivisionByZeroException('division by zero in VM')
                self.stk = self.stk.pop().pop().push(x % y)
                self.pc = self.pc + 1
            elif com.cname == CName.ADD:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for add')
                y = self.stk.top()
                x = self.stk.pop().top()
                self.stk = self.stk.pop().pop().push(x + y)
                self.pc = self.pc + 1
            elif com.cname == CName.SUB:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for sub')
                y = self.stk.top()
                x = self.stk.pop().top()
                self.stk = self.stk.pop().pop().push(x - y)
                self.pc = self.pc + 1
            elif com.cname == CName.EQ:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for eq')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == y:
                    self.stk = self.stk.pop().pop().push(1)
                else:
                    self.stk = self.stk.pop().pop().push(0)
                self.pc = self.pc + 1
            elif com.cname == CName.NEQ:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for neq')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == y:
                    self.stk = self.stk.pop().pop().push(0)
                else:
                    self.stk = self.stk.pop().pop().push(1)
                self.pc = self.pc + 1
            elif com.cname == CName.LT:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for lt')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x < y:
                    self.stk = self.stk.pop().pop().push(1)
                else:
                    self.stk = self.stk.pop().pop().push(0)
                self.pc = self.pc + 1
            elif com.cname == CName.GT:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for gt')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x > y:
                    self.stk = self.stk.pop().pop().push(1)
                else:
                    self.stk = self.stk.pop().pop().push(0)
                self.pc = self.pc + 1
            elif com.cname == CName.AND:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for and')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == 0 or y == 0:
                    self.stk = self.stk.pop().pop().push(0)
                else:
                    self.stk = self.stk.pop().pop().push(1)
                self.pc = self.pc + 1
            elif com.cname == CName.OR:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for or')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == 0 and y == 0:
                    self.stk = self.stk.pop().pop().push(0)
                else:
                    self.stk = self.stk.pop().pop().push(1)
                self.pc = self.pc + 1
            elif com.cname == CName.LOAD:
                try:
                    x = self.environment[com.name]
                    self.pc = self.pc + 1
                except KeyError:
                    raise UndefinedVariableException('undefined variable')
                self.stk = self.stk.push(x)
            elif com.cname == CName.STORE:
                if self.stk.is_empty():
                    raise VMError('stk is empty for store')
                self.environment[com.name] = self.stk.top()
                self.stk = self.stk.pop()
                self.pc = self.pc + 1
            elif com.cname == CName.JMP:
                self.pc = self.pc + com.num
            elif com.cname == CName.CJMP:
                if self.stk.is_empty():
                    raise VMError('stk is empty for cjmp')
                x = self.stk.top()
                self.stk = self.stk.pop()
                if x == 0:
                    self.pc = self.pc + 1
                else:
                    self.pc = self.pc + com.num
            elif com.cname == CName.QUIT:
                return self.environment
            else:
                raise VMError("An invalid command was met!")
        return self.environment
