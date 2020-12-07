with open('input.txt', 'r') as f:
    groups = f.read().split('\n\n')

# Part 1
acc = 0
for group in groups:
    acc += len(set(group.replace("\n", "")))

print("Part 1", acc)

# Part 2
acc2 = 0
for group in groups:
    people = list(map(set, group.split("\n")))
    acc2 += len(people[0].intersection(*people[1:]))
    
print("Part 2", acc2)