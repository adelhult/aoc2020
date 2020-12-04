with open("input.txt", "r") as f:
    m = [line.strip() for line in f]

def num_trees(m, xs, ys):
    max_x = len(m[0])
    trees = 0
    for x, y in enumerate(m[::ys]):
        if y[xs * x % max_x] == "#":
            trees += 1

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
