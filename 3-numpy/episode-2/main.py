import os
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for j in range(3):
    raw_data = np.loadtxt(os.path.join('signals', f'signal0{j + 1}.dat'))
    res_data = np.convolve(np.insert(raw_data, 0, np.zeros(9)), np.ones(10) / 10, mode='valid')[9:]
    start_data = np.matmul(np.tri(9, 9), raw_data[:9]) / np.arange(1, 10)
    axs[j].plot(raw_data, label='Сырой сигнал')
    axs[j].plot(np.append(start_data, res_data), label='После обработки')
    axs[j].set_title(f'Сигнал {j + 1}')
    axs[j].legend()
    axs[j].grid()

plt.savefig(f'signals.png')
plt.show()
