# just using a brute force method for part 2 instead:
from itertools import combinations 
numbers = [int(i) for i in open("input.txt").readlines()]

for i in combinations(numbers, 3):
    if i[0] + i[1] + i[2] == 2020:
        print(i[0] * i[1] * i[2])