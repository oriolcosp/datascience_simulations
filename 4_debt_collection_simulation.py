import numpy as np
import matplotlib.pyplot as plt

def simulate_collection(debt, prob_repay):
    num_companies = len(debt)
    did_repay = (np.random.rand(num_companies) < prob_repay)
    pct_paid = np.random.rand(num_companies)
    amount_collected = debt * did_repay * pct_paid
    return amount_collected.sum()

num_sims = 1000
amount_collected =
    np.array([simulate_collection(debt, prob_repay) for i in range(num_sims)])

print(f"Total debt: {np.round(amount_collected.mean())}$")
print(f"Average amount collected: {np.round(amount_collected.mean())}$")
percentile_95 = np.round(np.sort(amount_collected)[int(0.05*num_sims)])
print(f"95% percentile collection: {percentile_95}$")

plt.figure(figsize=[8,5])
plt.hist(amount_collected,bins=50)[2]