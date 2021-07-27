import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

def get_prob(elo1, elo2):
    return 1/(1+10**((elo2 - elo1)/400))

def update_elo(elo, prob, result, k):
    return elo + k * (result - prob)

def play_until_top(real_elo, initial_elo):
    current_elo = initial_elo
    num_games = 0
    k = 40
    elo_list = [initial_elo]
    while current_elo < real_elo:
        if num_games > 30:
            k = 20
        if current_elo > 2400:
            k = 10
        prob_win = get_prob(real_elo, current_elo)
        result = 1 if np.random.rand(1)[0] < prob_win else 0
        current_elo = update_elo(current_elo, 0.5, result, k)
        elo_list.append(current_elo)
        num_games += 1
    return elo_list

num_sims = 1000

num_games = [len(play_until_top(2847, 1000)) for i in range(num_sims)]
num_games = np.array(num_games)

print(num_games.mean())
plt.figure(figsize=[8,5])
plt.hist(num_games,bins=50)[2]

elo_history = np.array(play_until_top(2847, 1000))
plt.figure(figsize=[8,5])
plt.plot(np.arange(0, len(elo_history)), elo_history)
plt.show()