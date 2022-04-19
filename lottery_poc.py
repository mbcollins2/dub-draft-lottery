#####
# Script to replication NBA Lottery process for top 4 teams only
# https://www.nba.com/news/nba-draft-lottery-explainer
#####

import random
import itertools
from util import *

# generate lottery ball combinations
lottery_balls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
combinations = [c for c in itertools.combinations(lottery_balls, 4)]

# randomize combinations
random_state = 1234
randomized_combinations = random.sample(combinations, len(combinations))

# assign teams to combinations based on lottery percent [50%, 30%, 15%, 5%]
team_combinations = {}
num_valid_combinations = len(combinations)-1
# team_combinations['Easton'] = randomized_combinations[0:500] # 50% of randomized combinations
# team_combinations['Harrison'] = randomized_combinations[500:800] # 30% of randomized combinations
# team_combinations['Cooper'] = randomized_combinations[800:950] # 15% of randomized combinations
# team_combinations['Ryan'] = randomized_combinations[950:1000] # 5% of randomized combinations
# team_combinations['None'] = randomized_combinations[1000:] # 1 extra combination
team_combinations['Easton'] = randomized_combinations[0:(0.5*num_valid_combinations)] # 50% of randomized combinations
team_combinations['Harrison'] = randomized_combinations[(0.5*num_valid_combinations):((0.5)*num_valid_combinations)] # 30% of randomized combinations
team_combinations['Cooper'] = randomized_combinations[800:950] # 15% of randomized combinations
team_combinations['Ryan'] = randomized_combinations[950:1000] # 5% of randomized combinations
team_combinations['None'] = randomized_combinations[1000:] # 1 extra combination

# randomly sample for 1st pick





