import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Read the image
img = np.array(Image.open("img.jpg").convert("RGB"))

# Create output image
result = np.empty_like(img)

# Enhance each color channel
for i in range(3):
    color = img[:, :, i].astype(float)
    low = color.min()
    high = color.max()

    if high != low:
        result[:, :, i] = ((color - low) * 255 / (high - low)).astype(np.uint8)
    else:
        result[:, :, i] = color.astype(np.uint8)

# Show results
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(result)
axes[1].set_title("Enhanced Image")
axes[1].axis("off")

plt.show()