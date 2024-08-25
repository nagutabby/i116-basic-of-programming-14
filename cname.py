from enum import Enum, auto

class CName(Enum):
    PUSH = auto()
    LOAD = auto()
    STORE = auto()
    MONE = auto()
    MUL = auto()
    DIV = auto()
    REM = auto()
    ADD = auto()
    SUB = auto()
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    AND = auto()
    OR = auto()
    JMP = auto()
    CJMP = auto()
    QUIT = auto()
    NSC = auto()

    def __str__(self) -> str:
        if self == CName.PUSH:
            return 'push'
        elif self == CName.LOAD:
            return 'load'
        elif self == CName.STORE:
            return 'store'
        elif self == CName.MONE:
            return 'mone'
        elif self == CName.MUL:
            return 'mul'
        elif self == CName.DIV:
            return 'div'
        elif self == CName.REM:
            return 'rem'
        elif self == CName.ADD:
            return 'add'
        elif self == CName.SUB:
            return 'sub'
        elif self == CName.EQ:
            return 'eq'
        elif self == CName.NEQ:
            return 'neq'
        elif self == CName.LT:
            return 'lt'
        elif self == CName.GT:
            return 'gt'
        elif self == CName.AND:
            return 'and'
        elif self == CName.OR:
            return 'or'
        elif self == CName.JMP:
            return 'jmp'
        elif self == CName.CJMP:
            return 'cjmp'
        elif self == CName.QUIT:
            return 'quit'
        else:
            return 'noSuchCommand'
