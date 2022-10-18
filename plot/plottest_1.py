#!/usr/bin/python3
"""
testing live data vizualization
"""
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count


def animate(index):
    x.append(next(index))
    y.append(random.randint(0, 5))

    plt.cla()
    plt.plot(x, y)



def main():
    plt.style.use('fivethirtyeight')

    x = []
    y = []

    index = count()

    anim = FuncAnimation(plt.gcf(), animate, 1000)

    plt.tight_layout()
    plt.show()

    return anim


if __name__ == '__main__':
    main()


