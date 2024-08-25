from enum import *

class TName(Enum):
    """
    Token names used in Minila are defined.
    """
    SEMC = auto() # ;
    COL = auto() # :
    LPAR = auto() # (
    RPAR = auto() # )
    MUL = auto() # *
    QUO = auto() # /
    REM = auto() # %
    PLUS = auto() # +
    MINUS = auto() # -
    LT = auto() # <
    GT = auto() # >
    EQ = auto() # =
    NEQ = auto() # !=
    AND = auto() # &&
    OR = auto() # ||
    ASSIGN = auto() # :=
    IF = auto() # if
    THEN = auto() # then
    ELSE = auto() # else
    FI = auto() # fi
    WHILE = auto() # while
    FOR = auto() # for
    DO = auto() # do
    OD = auto() # od
    NUM = auto() # [0-9]+
    VAR = auto() # [a-zA-Z][a-zA-Z0-9]* except for keywords
    UNDEF = auto() # undefined tokens

    def __str__(self):
        if self == TName.SEMC:
            return ';'
        elif self == TName.COL:
            return ':'
        elif self == TName.LPAR:
            return '('
        elif self == TName.RPAR:
            return ')'
        elif self == TName.MUL:
            return '*'
        elif self == TName.QUO:
            return '/'
        elif self == TName.REM:
            return '%'
        elif self == TName.PLUS:
            return '+'
        elif self == TName.MINUS:
            return '-'
        elif self == TName.LT:
            return '<'
        elif self == TName.GT:
            return '>'
        elif self == TName.EQ:
            return '='
        elif self == TName.NEQ:
            return '!='
        elif self == TName.AND:
            return '&&'
        elif self == TName.OR:
            return '||'
        elif self == TName.ASSIGN:
            return ':='
        elif self == TName.IF:
            return 'if'
        elif self == TName.THEN:
            return 'then'
        elif self == TName.ELSE:
            return 'else'
        elif self == TName.FI:
            return 'fi'
        elif self == TName.WHILE:
            return 'while'
        elif self == TName.FOR:
            return 'for'
        elif self == TName.DO:
            return 'do'
        elif self == TName.OD:
            return 'od'
        elif self == TName.NUM:
            return 'num'
        elif self == TName.VAR:
            return 'var'
        else:
            return 'UNDEF'

"""
print(TName.SEMC.__str__())
print(TName.COL.__str__())
print(TName.LPAR.__str__())
print(TName.RPAR.__str__())
print(TName.MUL.__str__())
print(TName.QUO.__str__())
print(TName.REM.__str__())
print(TName.PLUS.__str__())
print(TName.MINUS.__str__())
print(TName.LT.__str__())
print(TName.GT.__str__())
print(TName.EQ.__str__())
print(TName.NEQ.__str__())
print(TName.AND.__str__())
print(TName.OR.__str__())
print(TName.ASSIGN.__str__())
print(TName.IF.__str__())
print(TName.THEN.__str__())
print(TName.ELSE.__str__())
print(TName.FI.__str__())
print(TName.WHILE.__str__())
print(TName.FOR.__str__())
print(TName.DO.__str__())
print(TName.NUM.__str__())
print(TName.VAR.__str__())
print(TName.UNDEF.__str__())

print(str(TName.SEMC))
print(str(TName.COL))
print(str(TName.LPAR))
print(str(TName.RPAR))
print(str(TName.MUL))
print(str(TName.QUO))
print(str(TName.REM))
print(str(TName.PLUS))
print(str(TName.MINUS))
print(str(TName.LT))
print(str(TName.GT))
print(str(TName.EQ))
print(str(TName.NEQ))
print(str(TName.AND))
print(str(TName.OR))
print(str(TName.ASSIGN))
print(str(TName.IF))
print(str(TName.THEN))
print(str(TName.ELSE))
print(str(TName.FI))
print(str(TName.WHILE))
print(str(TName.FOR))
print(str(TName.DO))
print(str(TName.NUM))
print(str(TName.VAR))
print(str(TName.UNDEF))
"""
