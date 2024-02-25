import matplotlib.pyplot as plt

r=2
if r < 25:
    r += 1
if r >= 25 and r != 5:
    r -= 1

plt.plot(r)