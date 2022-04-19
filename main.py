from lottery import draft_lottery

if __name__ == "__main__":
    draft = draft_lottery(draft_odds = {'Easton': 0.5, 'Ryan': 0.05, 'Harrison': 0.3, 'Cooper': 0.15})
    draft.randomize_draft_combinations()
    draft.draft()


    # print(draft.draft_odds)
    # print(draft.teams)
    # print(draft.team_odds)
    # print(draft.team_lottery_numbers)