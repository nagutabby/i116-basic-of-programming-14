from tname import *

class Token(object):
    """
    Tokens used in Minila are defind.
    There are two tokens that have a parameter: Num(n) and VAR(x),
    where n is an integer and x is a string used as a variable name.
    The other tokens, such as ADD and MUL, do not have.
    """
    tname = TName.UNDEF
    num = 0
    name = ''

    def __init__(self, tn, x):
        self.tname = tn
        if tn == TName.NUM:
            self.num = x
        elif tn == TName.VAR:
            self.name = x
        elif tn == TName.UNDEF:
            self.name = x

    def __str__(self):
        if self.tname == TName.NUM:
            return str(self.tname) + ': ' + str(self.num)
        elif self.tname == TName.VAR:
            return str(self.tname) + ': ' + str(self.name)
        elif self.tname == TName.UNDEF:
            return str(self.tname) + ': ' + str(self.name)
        else:
            return str(self.tname)

"""
print( str(Token(TName.SEMC,None)) )
print( str(Token(TName.MUL,None)) )
print( str(Token(TName.WHILE,None)) )
print( str(Token(TName.NUM,100)) )
print( str(Token(TName.VAR,'xyz')) )
"""
