with open("input.txt", "r") as f:
    m = [list(map(lambda i: i == "#", line.strip())) for line in f.readlines()]

def num_trees(m, xs, ys):
    max_x = len(m[0])
    x = 0
    trees = 0
    for y in m[::ys]:
        if y[xs * x % max_x]:
            trees += 1
        x += 1

    return trees

# part 1:
print(num_trees(m, 3, 1)) 

# part 2:
print(
        num_trees(m, 1, 1) *
        num_trees(m, 3, 1) *
        num_trees(m, 5, 1) *
        num_trees(m, 7, 1) *
        num_trees(m, 1, 2)
    )