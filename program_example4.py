from scan import *
from parse import *
from vm import *

isPrime = ' '\
' x := 119; '\
' y := 2; '\
' r := 1; '\
' f := 1; '\
' while f do '\
' if x % y = 0 '\
' then f := 0; '\
' r := 0; '\
' else y := y+1; fi '\
' if x = y then f := 0; else fi '\
' od '
tl = scan(isPrime)
tlo = TokenList(tl)
pt = tlo.parse()
cl = pt.gen_code()
print(l2s(cl))
print(VM(cl).run())
