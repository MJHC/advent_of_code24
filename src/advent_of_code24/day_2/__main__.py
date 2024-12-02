import os

DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    data = [list(map(lambda y: int(y), x.split())) for x in f.read().splitlines()]
    check = lambda f, xs: [f(x, xs[i + 1]) if i + 1 < len(xs) else f(xs[i - 1], x) for i, x in enumerate(xs)]
    
    
    decrease = lambda x, y: x > y and x - y <= 3
    increase = lambda x, y: x < y and y - x <=3
    is_safe = lambda xs: all(check(decrease, xs)) or all(check(increase, xs))
    
    remove = lambda xs, i: [x for j, x in enumerate(xs) if i != j]
    mutate = lambda xs: [remove(xs, i) for i in range(len(xs))]
    is_safe_dampening = lambda xs: any(is_safe(xss) for xss in mutate(xs))
    
    part_1 = list(filter(is_safe, data))
    part_2 = list(filter(is_safe_dampening, data))
    
print(len(part_1))
print(len(part_2))
    