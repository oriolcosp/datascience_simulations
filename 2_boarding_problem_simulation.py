import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

def simulate_boarding(num_passengers):
    passenger_seats = set(range(num_passengers))
    for i in range(num_passengers):
        if i == num_passengers - 1:
            if list(passenger_seats)[0] == i:
                return 1
            else:
                return 0
        if (i == 0) or (not i in passenger_seats):
            i = list(passenger_seats)[np.random.randint(0, num_passengers - i)]
            passenger_seats.remove(i)
        else:
            passenger_seats.remove(i)
        
num_sims = 10000
num_passengers = 100
positives = 0

is_same_seat = [simulate_boarding(num_passengers) for i in range(num_sims)]
is_same_seat = np.array(is_same_seat)


print(is_same_seat.mean())
plt.figure(figsize=[8,5])
one_to_n = np.arange(1, num_sims+1)
plt.plot(one_to_n, is_same_seat.cumsum() / one_to_n)
plt.show()