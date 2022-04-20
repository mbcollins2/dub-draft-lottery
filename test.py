from lottery import draft_lottery
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from collections import Counter

if __name__ == "__main__":

    counts = {team: [] for team in ['Easton', 'Harrison', 'Cooper', 'Ryan']}

    tests = 10000
    for i in range(tests):
        draft = draft_lottery(draft_odds = {'Easton': 0.5, 'Harrison': 0.3, 'Cooper': 0.15, 'Ryan': 0.05})
        draft.draft()

        for team in ['Easton', 'Harrison', 'Cooper', 'Ryan']:
            if draft.first_pick == team:
                counts[team].append(1)
            if draft.second_pick == team:
                counts[team].append(2)
            if draft.third_pick == team:
                counts[team].append(3)
            if draft.fourth_pick == team:
                counts[team].append(4)



    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    odds = ['50%', '30%', '15%', '5%']
    fig, ax = plt.subplots(4, 1, sharex=True, sharey=True)

    for i, team in enumerate(['Easton', 'Harrison', 'Cooper', 'Ryan']):
        cnt = Counter(counts[team])
        bars = ax[i].bar([str(c) for c in sorted(cnt)], [float(cnt[k]/tests*100) for k in sorted(cnt)], color=colors[i])
        ax[i].bar_label(bars, fmt='%.0f%%')
        ax[i].yaxis.set_major_formatter(mtick.PercentFormatter())
        ax[i].text(1.5, 80, f'{team} ({odds[i]})',
            fontsize=20, color=colors[i], alpha=0.5,
            ha='center', va='center')

    plt.suptitle('Simulated Draft Outcomes \n Odds of first pick: 50%, 30%, 15%, 5%', fontsize=18)
    plt.ylim(0,100)
    plt.xlabel('Pick')
    plt.show()
    







