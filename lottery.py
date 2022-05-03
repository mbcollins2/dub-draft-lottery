#####
# Class to replication NBA Lottery process for top 4 teams only
# https://www.nba.com/news/nba-draft-lottery-explainer
#####

import random
import itertools
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from collections import Counter
from decimal import Decimal

class draft_lottery(object):
    def __init__(self, draft_odds: dict) -> None:
        # define draft odds
        assert sum([Decimal(str(odd)) for odd in draft_odds.values()]) == 1.0, f'Values sum to {sum(draft_odds.values())}'
        self.draft_odds = sorted(draft_odds.items(), key=lambda x:x[1], reverse=True) # assure teams are sorted by draft 

        self.teams = [team[0] for team in self.draft_odds]
        self.team_odds = [Decimal(str(team[1])) for team in self.draft_odds]

        # define lottery parameters
        self.num_lottery_balls = 14
        self.num_lottery_balls_to_draw = 4
        self.lottery_balls = [x for x in range(1, self.num_lottery_balls+1)]
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
        self.first_pick = ''
        self.second_pick = ''
        self.third_pick = ''
        self.fourth_pick = ''

        # assign teams to lottery combinations
        self.team_lottery_numbers_prep = {}
        for i in range(len(self.teams)):
            self.team_lottery_numbers_prep[self.teams[i]] = self.randomized_combinations[int(sum(self.team_odds[:i])*self.num_valid_combinations):int(sum(self.team_odds[:i+1])*self.num_valid_combinations)]
        self.team_lottery_numbers_prep['None'] = self.randomized_combinations[self.num_valid_combinations:]

        self.team_lottery_numbers = {}
        for team in self.team_lottery_numbers_prep:
            for combination in self.team_lottery_numbers_prep[team]:
                self.team_lottery_numbers[combination] = team
        
        
        # first pick
        self.first_pick = self.team_lottery_numbers[self.draw_combination()]
        
        # second pick
        self.second_pick = self.first_pick
        while self.second_pick in [self.first_pick]:
            self.second_pick = self.team_lottery_numbers[self.draw_combination()]
        
        # second pick
        self.third_pick = self.first_pick
        while self.third_pick in [self.first_pick, self.second_pick]:
            self.third_pick = self.team_lottery_numbers[self.draw_combination()]
        
        # second pick
        self.fourth_pick = self.first_pick
        while self.fourth_pick in [self.first_pick, self.second_pick, self.third_pick]:
            self.fourth_pick = self.team_lottery_numbers[self.draw_combination()]


    def simulate_draft(self, n=1000):
        counts = {team: [] for team in self.teams}

        for i in range(n):
            self.randomize_draft_combinations()
            self.draft()

            for team in self.teams:
                if self.first_pick == team:
                    counts[team].append(1)
                if self.second_pick == team:
                    counts[team].append(2)
                if self.third_pick == team:
                    counts[team].append(3)
                if self.fourth_pick == team:
                    counts[team].append(4)

        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        odds = [f'{odd*100:,.0f}%' for odd in self.team_odds]
        fig, ax = plt.subplots(4, 1, sharex=True, sharey=True)

        for i, team in enumerate(self.teams):
            cnt = Counter(counts[team])
            bars = ax[i].bar([str(c) for c in sorted(cnt)], [float(cnt[k]/n*100) for k in sorted(cnt)], color=colors[i])
            ax[i].bar_label(bars, fmt='%.0f%%')
            ax[i].yaxis.set_major_formatter(mtick.PercentFormatter())
            ax[i].text(1.5, 80, f'{team} ({odds[i]})',
                fontsize=20, color=colors[i], alpha=0.5,
                ha='center', va='center')
            # ax[i].set(ylabel='% of drafts receiving pick')

        plt.suptitle(f'Simulated Draft Outcomes (n={n})', fontsize=18)
        plt.ylim(0,100)
        plt.xlabel('Pick')
        plt.show()


        

        





