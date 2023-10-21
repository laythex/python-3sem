import os
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 3, figsize=(12, 8))

for i in range(5):
    points = []
    with open(os.path.join('dead_moroz', f'00{i + 1}.dat')) as file:
        n = int(file.readline())
        for j in range(n):
            points.append(list(map(float, file.readline().split())))

    axs[i // 3][i % 3].scatter(*zip(*points), s=5)
    axs[i // 3][i % 3].set_title(f'Number of points: {n}')
    axs[i // 3][i % 3].set_aspect('equal')

axs[1][2].axis('off')

plt.savefig('episode-1.png')
plt.show()
