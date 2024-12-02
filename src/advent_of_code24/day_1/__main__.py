import os

DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    data = f.read().replace("\n", " ").split()
    extract = lambda d, j: [int(x) for i, x in enumerate(d) if i % 2 == j]
    
    xs = sorted(extract(data, 0))
    ys = sorted(extract(data, 1))
    part_1 = sum(abs(x - y) for (x, y) in zip(xs, ys))
    part_2 = sum(x * len([y for y in ys if y == x]) for x in xs)
    

print(part_1)
print(part_2)