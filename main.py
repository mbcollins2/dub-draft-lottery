from lottery import draft_lottery

if __name__ == "__main__":
    draft = draft_lottery(draft_odds = {'Easton': 0.5, 'Harrison': 0.3, 'Cooper': 0.15, 'Ryan': 0.05})
    # draft = draft_lottery(draft_odds = {'OJ': 0.30, 'NN': 0.30, 'BF': 0.30, 'HR': 0.10})

    draft.simulate_draft(10000)

    # draft.draft()
    # print(f'First Pick: {draft.first_pick}')
    # print(f'Second Pick: {draft.second_pick}')
    # print(f'Third Pick: {draft.third_pick}')
    # print(f'Fourth Pick: {draft.fourth_pick}')







