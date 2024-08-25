from scan import *
from parse import *

fact = ' '\
' x := 1;'\
' y := 1;'\
' while y < 5'\
' do'\
' x := x * y;'\
' y := y + 1;'\
' od'
tl = scan(fact)
tlo = TokenList(tl)
pt = tlo.parse()

print(fact)
print(l2s(tl))
print(pt)

print(pt.interpret({ }))
