import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def animate(i):
    data = open('example.txt', 'r').read()
    lines = data.split("\n")
    x_values = []
    y_values = []
    for line in lines:
        x,y = line.split(',')
        x_values.append(x)
        y_values.append(y)
    ax.plot(x_values, y_values)

ani = animation.FuncAnimation(fig, animate, interval=1000 )
plt.show()
