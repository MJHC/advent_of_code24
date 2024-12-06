import os
import math
DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    rules, updates = f.read().split("\n\n")
    rules = [tuple(map(int, x.split("|"))) for x in rules.split("\n")]
    updates = [list(map(int, x.split(","))) for x in updates.split("\n")]
    
    index = lambda xs, y: next((i for i, x in enumerate(xs) if x == y), None)
    indice = lambda xs, rs: (list(filter(
        lambda x: not any(y is None for y in x) and x[0] > x[1], 
        [(index(xs, r[0]), index(xs, r[1])) for r in rs])))
    
    is_valid = lambda xs, rs: all([r[0] < r[1] for r in indice(xs, rs)])
    error_updates = lambda xs, rs: list(filter(lambda x: not is_valid(x, rs), xs))
    
    swap = lambda xs, i ,j: [*xs[:i], xs[j], *xs[i+1:j], xs[i], *xs[j + 1:]] if all(0 <= x < len(xs) for x in [i, j]) else xs
    apply_rule = lambda xs, r: swap(xs, r[1], r[0])
    
    fix_update = lambda xs, rs: fix_update(apply_rule(xs, indice(xs, rs)[0]), rs) if len(indice(xs, rs)) > 0 else xs
    fix_updates = lambda xss, rs: [fix_update(xs, rs) for xs in error_updates(xss, rs)]
    
    middles = lambda xss: [xs[math.floor(len(xs) / 2)] for xs in xss]
    
    fixed = fix_updates(updates, rules)
    part_1 = sum(middles(filter(lambda xs: is_valid(xs, rules), updates)))
    part_2 = sum(middles(fix_updates(updates, rules)))
    
    print(part_1)
    print(part_2)
    