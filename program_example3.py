from scan import *
from parse import *
from vm import *

gcd = ' '\
' x := 19110; '\
' y := 17850; '\
' while y != 0 do '\
' tmp := x%y; '\
' x := y; '\
' y := tmp; '\
' od '
tl = scan(gcd)
tlo = TokenList(tl)
pt = tlo.parse()
cl = pt.gen_code()
print(l2s(cl))
print(VM(cl).run())
