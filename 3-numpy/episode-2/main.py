import os
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for j in range(3):
    raw_data = np.loadtxt(os.path.join('signals', f'signal0{j + 1}.dat'))
    res_data = np.zeros_like(raw_data)
    for i in range(len(res_data)):
        res_data[i] = np.mean(raw_data[max(0, i - 9):i + 1])

    axs[j].plot(raw_data, label='Сырой сигнал')
    axs[j].plot(res_data, label='После обработки')
    axs[j].set_title(f'Сигнал {j + 1}')
    axs[j].legend()
    axs[j].grid()

plt.savefig(f'signals.png')
plt.show()
