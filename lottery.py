#####
# Class to replication NBA Lottery process for top 4 teams only
# https://www.nba.com/news/nba-draft-lottery-explainer
#####

import random
import itertools

class draft_lottery(object):
    def __init__(self, draft_odds: dict) -> None:
        # define draft odds
        assert sum(draft_odds.values()) == 1.0
        self.draft_odds = sorted(draft_odds.items(), key=lambda x:x[1], reverse=True) # assure teams or sorted by draft odds

        self.teams = [team[0] for team in self.draft_odds]
        self.team_odds = [team[1] for team in self.draft_odds]

        # define lottery parameters
        self.num_lottery_balls = 14
        self.num_lottery_balls_to_draw = 4
        self.lottery_balls = [x for x in range(self.num_lottery_balls)]
        self.lottery_combinations = [c for c in itertools.combinations(self.lottery_balls, 4)]
        self.randomized_combinations = random.sample(self.lottery_combinations, len(self.lottery_combinations))
        self.num_valid_combinations = len(self.lottery_combinations)-1


    def draw_lottery_ball(self, drawn: list = []) -> int:
        return random.sample([x for x in range(1,self.num_lottery_balls+1) if x not in drawn],1)[0]


    def draw_combination(self):
        drawn = []

        while len(drawn) < self.num_lottery_balls_to_draw:
            lottery_ball = self.draw_lottery_ball(drawn=drawn)
            drawn.append(lottery_ball)

        return tuple(sorted(drawn))


    def randomize_draft_combinations(self):
        self.randomized_combinations = random.sample(self.lottery_combinations, len(self.lottery_combinations))


    def draft(self):
        # assign teams to lottery combinations
        self.team_lottery_numbers_prep = {}
        for i in range(len(self.teams)):
            self.team_lottery_numbers_prep[self.teams[i]] = self.randomized_combinations[int(sum(self.team_odds[:i])*self.num_valid_combinations):int(sum(self.team_odds[:i+1])*self.num_valid_combinations)]
        self.team_lottery_numbers_prep['None'] = self.randomized_combinations[self.num_valid_combinations:]

        self.team_lottery_numbers = {}
        for team in self.team_lottery_numbers_prep:
            for combination in self.team_lottery_numbers_prep[team]:
                self.team_lottery_numbers[combination] = team

        print(len(self.team_lottery_numbers))

        # TODO - getting error here, not finding some combinations
        # first pick
        # self.first_pick = self.team_lottery_numbers[self.draw_combination()]
        # print(self.first_pick)

        # TODO - for subsequent picks, need to add a while loop to check if the combo was already drawn and if so redraw


        

        





