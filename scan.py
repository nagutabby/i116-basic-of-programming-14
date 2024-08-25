from list_to_string import *
from tname import *
from token2 import *

def toToken(w):
    """
    It converts a string that has no delimiter into a token.
    """
    if w == '':
        return Token(TName.UNDEF,'')
    elif w == 'if':
        return Token(TName.IF,None)
    elif w == 'then':
        return Token(TName.THEN,None)
    elif w == 'else':
        return Token(TName.ELSE,None)
    elif w == 'fi':
        return Token(TName.FI,None)
    elif w == 'for':
        return Token(TName.FOR,None)
    elif w == 'while':
        return Token(TName.WHILE,None)
    elif w == 'do':
        return Token(TName.DO,None)
    elif w == 'od':
        return Token(TName.OD,None)
    elif w.isascii() and w.isdecimal():
        return Token(TName.NUM,int(w))
    elif w.isascii() and w[0].isalpha() and w.isalnum():
        return Token(TName.VAR,w)
    else:
        return Token(TName.UNDEF,w)


"""
print(str(toToken("123")))
print(str(toToken("while")))
print(str(toToken("ab23")))
"""

def scan(sc):
    """
    It converts a string sc into a list of tokens.
    """
    tl = []
    word = ''
    idx = 0
    c = ''
    while idx < len(sc):
        c = sc[idx]
        idx = idx + 1
        if c == ' ' or c == '\t' or c == '\n' or c == '\r':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            continue
        if c == ';':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.SEMC,None))
        elif c == '(':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.LPAR,None))
        elif c == ')':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.RPAR,None))
        elif c == '*':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.MUL,None))
        elif c == '/':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.QUO,None))
        elif c == '%':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.REM,None))
        elif c == '+':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.PLUS,None))
        elif c == '-':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.MINUS,None))
        elif c == '<':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.LT,None))
        elif c == '>':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.GT,None))
        elif c == '=':
            if len(word) != 0:
                tl.append(toToken(word))
                word = ''
            tl.append(Token(TName.EQ,None))
        elif c == '!':
            if idx == len(sc):
                word = word + c
            elif sc[idx] == '=':
                if len(word) != 0:
                    tl.append(toToken(word))
                    word = ''
                tl.append(Token(TName.NEQ,None))
                idx = idx + 1
            else:
                 word = word + c
        elif c == '&':
            if idx == len(sc):
                word = word + c
            elif sc[idx] == '&':
                if len(word) != 0:
                    tl.append(toToken(word))
                    word = ''
                tl.append(Token(TName.AND,None))
                idx = idx + 1
            else:
                 word = word + c
        elif c == '|':
            if idx == len(sc):
                word = word + c
            elif sc[idx] == '|':
                if len(word) != 0:
                    tl.append(toToken(word))
                    word = ''
                tl.append(Token(TName.OR,None))
                idx = idx + 1
            else:
                 word = word + c
        elif c == ':':
            if idx == len(sc):
                word = word + c
            elif sc[idx] == '=':
                if len(word) != 0:
                    tl.append(toToken(word))
                    word = ''
                tl.append(Token(TName.ASSIGN,None))
                idx = idx + 1
            else:
                 word = word + c
        else:
            word = word + c
    if len(word) != 0:
        tl.append(toToken(word))
        word = ''
    return tl

"""
sr20000 = 'v0 := 20000;'\
'                     v1 := 0;'\
'                     v2 := v0;'\
'                     while v1 != v2 do'\
'                         if (v2-v1)%2 = 0'\
'                         then v3 := v1+(v2-v1)/2;'\
'                         else v3 := v1+(v2-v1)/2+1;'\
'                         fi'\
'                         if v3*v3 > v0'\
'                         then v2 := v3-1;'\
'                         else v1 := v3;'\
'                         fi'\
'                     od'

print( sr20000 )
print( ' ' )
print( scan(sr20000) )
print( ' ' )
print( l2s(scan(sr20000)) )

print( scan("abc") )
print( l2s(scan("abc")) )
print( '' == '' )
print( l2s([Token(TName.SEMC,None), Token(TName.WHILE,None), Token(TName.VAR,'xyz')]) )
"""
