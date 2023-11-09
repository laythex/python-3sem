import os
import numpy as np
from PIL import Image

for i in range(1, 4):
    data = np.array(Image.open(os.path.join('lunar_images', f'lunar0{i}_raw.jpg')))

    min_val, max_val = data.min(), data.max()
    data = (255 / (max_val - min_val) * (data - min_val)).astype(np.uint8)

    res = Image.fromarray(data)
    res.save(f'lunar0{i}.jpg')
