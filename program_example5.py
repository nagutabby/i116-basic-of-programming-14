from scan import *
from parse import *
from vm import *

sr = ' '\
' v0 := 20000000000000000; '\
' v1 := 0; '\
' v2 := v0; '\
' while v1 != v2 do '\
' if (v2-v1)%2 = 0 '\
' then v3 := v1+(v2-v1)/2; '\
' else v3 := v1+(v2-v1)/2+1; '\
' fi '\
' if v3*v3 > v0 '\
' then v2 := v3-1; '\
' else v1 := v3; '\
' fi '\
' od '
tl = scan(sr)
tlo = TokenList(tl)
pt = tlo.parse()
cl = pt.gen_code()
print(l2s(cl))
print(VM(cl).run())
