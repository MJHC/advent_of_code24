import os
import re

DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    data = f.read()
    
    
    _extract = lambda xs, ys, z: (
            xs 
            if len(ys) == 0
            else 
            _extract(xs, ys[1:], True)
            if ys[0] == "do()"
            else
            _extract(xs, ys[1:], False)
            if ys[0] == "don't()" or not z
            else
            _extract([*xs, ys[0]], ys[1:], z)
            )
    

    extract = lambda xs: _extract([], xs, True)
    
    convert = lambda xs: [x.replace("mul(", "").replace(")", "").split(",") for x in xs]
    evaluate = lambda xs: sum(map(lambda y: int(y[0]) * int(y[1]), convert(xs)))
    
    part_1 = evaluate(re.findall(r"mul\(\d{1,3},\d{1,3}\)", data))
    
    feature = extract(re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", data))

    part_2 = evaluate(feature)
    print(part_1)
    print(part_2)
