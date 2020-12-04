from passport import Passport as P

with open("input.txt", "r") as f:
    document = f.read()

# only part 2 in this file:
nr_valid = sum([p.valid() for p in P.read(document)])
print(nr_valid)
