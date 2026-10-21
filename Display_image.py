import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt

# 1. Load the image and convert to RGB
image = Image.open("download (7).jpg").convert("RGB")
img = np.array(image)

# 2. Perform contrast stretching channel by channel
stretched = np.zeros_like(img)
for i in range(3):
    channel = img[:, :, i].astype(np.float32)
    r_min = np.min(channel)
    r_max = np.max(channel)
    
    if r_max > r_min:
        stretched[:, :, i] = np.clip((channel - r_min) * 255.0 / (r_max - r_min), 0, 255).astype(np.uint8)
    else:
        stretched[:, :, i] = channel.astype(np.uint8)

# 3. Plot side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(stretched)
plt.title("Contrast Stretched Image")
plt.axis("off")

plt.tight_layout()
plt.show()