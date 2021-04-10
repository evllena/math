from matplotlib import pyplot as plt


circle = plt.Circle((0, 0), 5, fill=False)
ax = plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.grid(color='lightgray',linestyle='--')
plt.show()