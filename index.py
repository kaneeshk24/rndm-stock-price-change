import numpy as np
import matplotlib.pyplot as plt


# given probability
p_up = 0.5
p_down = 0.5


# simulate 10000 stock price changes
n_days = 10000
stock_changes = np.random.choice([-1, 1], size=n_days, p=[p_down, p_up])


# calculate the total stock price change (Xn)
stock_prices = np.cumsum(stock_changes)


# plot Xn vs n
plt.plot(range(n_days), stock_prices)
plt.xlabel("day") #--> n
plt.ylabel("stock price change") #-->Xn
plt.title("simulated stock price changes (10000 days)")
plt.grid(True)
plt.show()
