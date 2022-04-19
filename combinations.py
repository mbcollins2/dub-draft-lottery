import itertools

lottery_balls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print(len([c for c in itertools.combinations(lottery_balls, 4)]))

