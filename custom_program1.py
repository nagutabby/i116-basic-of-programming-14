from scan import *
from parse import *
from vm import *

sr = ' '\
'x := 10;'\
'y := x * 2;'\
'z := y / x;'

tl = scan(sr)
tlo = TokenList(tl)
pt = tlo.parse()
cl = pt.gen_code()
print(l2s(cl))
print(VM(cl).run())
