import os
from itertools import product
DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    equations = list(map(lambda x: (int(x[0]), list(map(int, x[1].strip().split(" ")))),map(lambda x: x.split(":"), f.read().splitlines())))
    flatten = lambda xss: [x for xs in xss for x in xs]
    fold_once = lambda xs, f: [f(xs[0], xs[1]), *xs[2:]] if len(xs) >= 2 else xs
    
    add = lambda x, y: x + y
    str_add = lambda x, y: int(str(x) + str(y))
    mul = lambda x, y: x * y
    
    fold_li = lambda xs, fs: fold_li(fold_once(xs, fs[0]), fs[1:]) if len(xs) != 1 and len(fs) != 0 else xs
    op_combo = lambda xs, fs: list(map(list, product(fs, repeat=len(xs) - 1)))
    fold_many = lambda xs, fss: flatten([fold_li(xs, fs) for fs in fss])
    
    fold_equation = lambda y, xs, fs: next((x for x in fold_many(xs, op_combo(xs, fs)) if x == y), 0)
    
    part_1 = sum(map(lambda x: fold_equation(*x, [add, mul]), equations))
    part_2 = sum(map(lambda x: fold_equation(*x, [add, mul, str_add]), equations))
    print(part_1)
    print(part_2)
