import time
from lottery import draft_lottery

if __name__ == "__main__":
    sleep_time = 5

    draft = draft_lottery(draft_odds = {'Team 1': 0.5, 'Team 2': 0.3, 'Team 3': 0.15, 'Team 4': 0.05})
    # draft = draft_lottery(draft_odds = {'Easton': 0.5, 'Harrison': 0.3, 'Cooper': 0.15, 'Ryan': 0.05})
    
    # draft.simulate_draft(10000)

    draft.draft()
    print(f'Fourth Pick: {draft.fourth_pick}')
    time.sleep(sleep_time)
    print(f'Third Pick: {draft.third_pick}')
    time.sleep(sleep_time)
    print(f'Second Pick: {draft.second_pick}')
    time.sleep(sleep_time)
    print(f'First Pick: {draft.first_pick}')







