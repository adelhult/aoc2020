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
    people = group.split("\n")
    shared_answers = set(people[0].strip())
    for person in people[1:]:
        shared_answers = shared_answers.intersection(set(person))

    acc2 += len(shared_answers)
    
print("Part 2", acc2)