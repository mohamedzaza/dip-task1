import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open(r"image.png").convert("RGB")
img = np.array(image)
stretched = np.zeros_like(img)

for c in range(3):
    channel = img[:, :, c].astype(np.float32)
    
    r_min = np.min(channel)
    r_max = np.max(channel)
    
    if r_max > r_min:
        stretched[:, :, c] = np.clip((channel - r_min) * 255.0 / (r_max - r_min), 0, 255).astype(np.uint8)
    else:
        stretched[:, :, c] = channel.astype(np.uint8)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Color Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(stretched)
plt.title("Contrast-Stretched Color Image")
plt.axis("off")
plt.tight_layout()
plt.show()