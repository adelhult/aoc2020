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
    shared_answers = list(set(people[0].strip()))
    to_remove = []
    if len(people) == 1:
        acc2 += len(shared_answers)
        continue
    for person in people:
        for answer in shared_answers:
            if answer not in list(person):
                to_remove.append(answer)  
    count = len([a for a in shared_answers if a not in to_remove])          
    acc2 += count
    
print("Part 2", acc2)