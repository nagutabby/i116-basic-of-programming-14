from scan import *
from parse import *
from vm import *

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
cl = pt.gen_code()
print(l2s(cl))
print(VM(cl).run())
