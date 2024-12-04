import os
DIR = os.path.dirname(__file__)

with open(os.path.join(DIR, "input.txt"), "r") as f:
    grid = f.read().splitlines()

    flatten = lambda xss: [x for xs in xss for x in xs]
    locate = lambda g, s: [(i, j) for i, gs in enumerate(g) for j, x in enumerate(gs) if x == s]
    walk = lambda g, p, v, m: g[p[0]][p[1]] + walk(g, (p[0] + v[0], p[1] + v[1]), v, m - 1) if 0 <= p[0] < len(g) and 0 <= p[1] < len(g[p[0]]) and m > 0 else ""

    north = lambda g, p: walk(g, p, (-1, 0), 4)
    south = lambda g, p: walk(g, p, (+1, 0), 4)
    west = lambda g, p: walk(g, p, (0, -1), 4)
    east = lambda g, p: walk(g, p, (0, +1), 4)
    northwest = lambda g, p: walk(g, p, (-1, -1), 4)
    northeast = lambda g, p: walk(g, p, (-1, +1), 4)
    southwest = lambda g, p: walk(g, p, (+1, -1), 4)
    southeast = lambda g, p: walk(g, p, (+1, +1), 4)

    explore = lambda g, p: [f(g, p) for f in [north, south, west, east, northwest, northeast, southwest, southeast]]
    explore_from = lambda g, s: [explore(g, p) for p in locate(g, s)]
    explore_xmas = lambda g: list(filter(lambda x: x == "XMAS", flatten(explore_from(g, "X"))))

    mas_crop = lambda xs: [y[1] if 1 < len(y) else y[0] for y in xs]
    mas_pack = lambda xs: xs[4] + xs[5] + xs[6] + xs[7]
    mas_filter = lambda x: x in ["MSMS", "SMSM", "MMSS", "SSMM"]
    explore_mas = lambda g: list(filter(mas_filter, map(mas_pack, map(mas_crop, explore_from(g, "A")))))

    print(len(explore_xmas(grid)))
    print(len(explore_mas(grid)))
    