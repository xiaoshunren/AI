import matplotlib.pyplot as plt

x = [0, 1]
y = [0, 1]
z = [0, 1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': '3d'})
ax.scatter(x, y, [1.0, 1.0], s=100, marker="o")
ax.scatter(x, y, [0.8, 0.8], s=100, marker="v")
ax.scatter(x, y, [0.6, 0.6], s=100, marker="s")
ax.scatter(x, y, [0.4, 0.4], s=100, marker="o")
ax.scatter(x, y, [0.2, 0.2], s=100, marker="D")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()