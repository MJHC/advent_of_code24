import os
DIR = os.path.dirname(__file__)

def predict(guard: tuple[int, int], velocity: tuple[int, int], boxes: list[tuple[int, int]], dim: tuple[int, int]):
    rotate = lambda xv: (0*xv[0] + 1 * xv[1], -1*xv[0] + 0*xv[1])
    is_inside = lambda p, dim: 0 <= p[0] < dim[0] and 0 <= p[1] < dim[1]
    rv = [guard]
    box_counter = {b: 0 for b in boxes}
    while is_inside(guard, dim):
        lookahead = guard[0] + velocity[0], guard[1] + velocity[1]
        if not is_inside(lookahead, dim):
            break
        if lookahead in boxes:
            velocity = rotate(velocity)
            box_counter[lookahead] += 1
            if box_counter[lookahead] > 5:
                return []
        else:
            guard = lookahead
            
        rv.append(guard)
    return rv

with open(os.path.join(DIR, "input.txt"), "r") as f:
    grid = list(map(list, f.read().splitlines()))
    locate = lambda g, s: [(i, j) for i, gs in enumerate(g) for j, x in enumerate(gs) if x == s]
    state = lambda g: (next(iter(locate(g, "^"))), (-1, 0), set(locate(g, "#")), (len(g), len(g[0])))
    
    g, v, b, d = state(grid)
    route = predict(g, v, b, d)
    part_1 = len(set(route))
    part_2 = 0
    mutated = ({x, *b} for x in set(route) if x != g)
    for boxes in mutated:
        if len(predict(g, v, boxes, d)) == 0:
            part_2 += 1
    
    print(part_1)
    print(part_2)
