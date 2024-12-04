import os
from pprint import pprint
DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    data = f.read().splitlines()
    
    indices = lambda xss, y: [(i, j) for i, xs in enumerate(xss) for j, x in enumerate(xs) if x == y]
    
    up = lambda xss, i, j: xss[i][j] + xss[i - 1][j] + xss[i - 2][j] + xss[i - 3][j] if 0 <= i - 3 < len(xss) and j < len(xss[i - 3]) else ""
    left = lambda xss, i, j: xss[i][j] + xss[i][j - 1] + xss[i][j - 2] + xss[i][j - 3] if i < len(xss) and 0 <= j - 3 < len(xss[i]) else ""
    left_top = lambda xss, i, j: xss[i][j] + xss[i - 1][j - 1] + xss[i - 2][j - 2] + xss[i - 3][j - 3] if 0 <= i - 3 < len(xss) and 0 <= j - 3 < len(xss[i - 3]) else ""
    right_top = lambda xss, i, j: xss[i][j] + xss[i - 1][j + 1] + xss[i - 2][j + 2] + xss[i - 3][j + 3] if 0 <= i - 3 < len(xss) and j + 3 < len(xss[i - 3]) else ""
    
    right_bot = lambda xss, i, j: xss[i][j] + xss[i + 1][j + 1] + xss[i + 2][j + 2] + xss[i + 3][j + 3] if i + 3 < len(xss) and j + 3 < len(xss[i + 3]) else ""
    left_bot = lambda xss, i, j: xss[i][j] + xss[i + 1][j - 1] + xss[i + 2][j - 2] + xss[i + 3][j - 3] if i + 3 < len(xss) and 0 <= j - 3 < len(xss[i - 3]) else ""
    right = lambda xss, i, j: xss[i][j] + xss[i][j + 1] + xss[i][j + 2] + xss[i][j + 3] if i < len(xss) and j + 3 < len(xss[i]) else ""
    down = lambda xss, i, j: xss[i][j] + xss[i + 1][j] + xss[i + 2][j] + xss[i + 3][j] if i + 3 < len(xss) and j < len(xss[i + 3]) else ""

    scan_xmas = lambda xss, i, j: [(f(xss, i, j), (i,j)) for f in [up, left, left_top, right_top, right_bot, left_bot, right, down]]
    
    top_mas = lambda xss, i, j: xss[i - 1][j - 1] + "." + xss[i - 1][j + 1] if 0 <= j - 1 and 0 <= i - 1 and i + 1 < len(xss) and j + 1 < len(xss[i - 1]) else ""
    bot_mas = lambda xss, i, j: xss[i + 1][j - 1] + "." + xss[i + 1][j+1] if 0 <= j - 1 and i + 1 < len(xss) and j + 1 < len(xss[i + 1]) else ""
    x_mas = lambda xss, i, j: [(top_mas(xss, i, j), bot_mas(xss, i, j))]
    
    flatten = lambda xss: [x for xs in xss for x in xs]
    check = lambda xss, f, g: flatten(f(xss, i, j) for i, j in g(xss))

    count_xmas = lambda xss: len(list(filter(lambda x: x[0] == "XMAS", check(xss, scan_xmas, lambda xss: indices(xss, "X")))))
    
    check_x_mas = lambda x: "|".join(x) in ["M.S|M.S", "S.M|S.M", "M.M|S.S", "S.S|M.M"]
    count_x_mas = lambda xss: len(list(filter(check_x_mas, check(xss, x_mas, lambda xss: indices(xss, "A")))))
    
    part_1 = count_xmas(data)
    part_2 = count_x_mas(data)
    
    print(part_1)
    print(part_2)