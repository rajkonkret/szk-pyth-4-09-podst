def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)  # a, b 1 2
allparams(1, 2, 3)  # c, d 3 256
allparams(1, 2, 3, 4)  # args (4,)
allparams(1, 2, 3, 4)  # args (4,)
allparams(1, 2, 3, 4)  # args (4,)
allparams(1, 2, 3, 4)  # args (4,)
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  # args (4, 5, 6, 7, 8, 9, 0)
# allparams(1, 2, c=9, 1, 2, 3, 4, 5)  # SyntaxError: positional argument follows keyword argument
allparams(1, 2, c=8)  # c, d 8 256
# allparams(a=1, b=2, c=3)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / odziela argumnty pozycyjne od nazwancy, czyli a i b mogą byc podane tylko w kolejnosci,
# nie mogą byc podane po nazwie
allparams(1, 2, 3, a=1)  # kwargs {'a': 1}
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16)
# args (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16)
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, d=34)
# c, d 3 34 - d musi być podany po nazwie
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, d=34, e=34, f=89, name="Radek")
# kwargs {'e': 34, 'f': 89, 'name': 'Radek'}
