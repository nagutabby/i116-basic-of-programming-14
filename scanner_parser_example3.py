from scan import *
from parse import *

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

print(gcd)
print(l2s(tl))
print(pt)

print(pt.interpret({ }))
