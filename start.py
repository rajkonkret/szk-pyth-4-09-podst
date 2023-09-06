import pakiet  # importuje zezwolone w __all__
from pakiet import fun
import pakiet.fun as pk  # import jako alias

print(pakiet)
# <module 'pakiet' from '/Users/radoslawjaniak/PycharmProjects/szk-pyth-4-09-pods/pakiet/__init__.py'>
# print(fun)
# <module 'pakiet.fun' from '/Users/radoslawjaniak/PycharmProjects/szk-pyth-4-09-pods/pakiet/fun.py'>
pakiet.fun.powitanie()  # niepotrzebnie uzyte pakiet
fun.powitanie()
pakiet.powitanie()
fun.info()
pk.info()
# 14:50