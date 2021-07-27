import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

def generate_synthetic_portfolio(num_companies):
    debt = 100000 * np.random.weibull(0.75, num_companies)
    
    prob_repayment = np.random.normal(0.2, 0.1, num_companies)
    prob_repayment = np.clip(prob_repayment, a_min=0, a_max=1)
    
    return debt, prob_repayment

num_companies = 1000
debt, prob_repayment = generate_synthetic_portfolio(num_companies)