import random


def draw_lottery_ball(num_lottery_balls: int = 14, drawn: list = []) -> int:
    return random.sample([x for x in range(1,num_lottery_balls+1) if x not in drawn],1)[0]


def draw_combination(num_lottery_balls_to_draw: int = 4):
    drawn = []

    while len(drawn) < num_lottery_balls_to_draw:
        lottery_ball = draw_lottery_ball(drawn=drawn)
        drawn.append(lottery_ball)

    return sorted(drawn)


# if __name__ == '__main__':
#     # print(draw_lottery_ball())
#     print(draw_combination())
