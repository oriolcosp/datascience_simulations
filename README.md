# Simulations for data science

Simulation is a skill that is missing from many data scientist's toolkits.

This repository contains the code for some examples of simulation problems that can be solved by a data scientist:

## Example 1. Estimate the value of pi by using simulation

## Example 2. Solve this problem by P. Winkler:
One hundred people line up to board an airplane. Each has a boarding pass with an assigned seat. However, the first person to board has lost his boarding pass and takes a random seat. After that, each person takes the assigned seat if it is unoccupied, and one of the unoccupied seats at random otherwise. What is the probability that the last person to board gets to sit in his assigned seat?

## Example 3. How many games would it take Magnus Carlsen (Elo of 2847 as of 18-07-2021) to get back to his current rating if he was dropped at 1000?

## Example 4. Solve the following business problem
Collectors LTD is a debt collection company focused on enterprise debt. It buys portfolios of business loans that have defaulted at some point and tries to collect the payments for those loans. Some of the companies will be bankrupt and won't be able to pay, and others are likely to go bankrupt in the future. The key to Collectors LTD’s business is in estimating the value it can get back from a portfolio. For this reason, Collectors LTD has developed a model that predicts the probability of a company repaying part of that debt. Among those companies that repay some of the debt, the amount paid is distributed uniformly from 0% to 100%. Collectors LTD can use its model in combination with simulation to evaluate the expected return of the portfolio, and how volatile that return is.
Since I can't share the real data with you, I've created a synthetic dataset that mimics the relevant properties, you can find the code that generates it it on the synthetic_debt_collection.py file.
Given the synthetically generated portfolio, estimate the expected amount to be collected and the 95% percentile.


You can find a full article with detailed explanations of the solutions of the problem here: https://oriolcosp.com/how-to-use-simulations-in-data-science.
