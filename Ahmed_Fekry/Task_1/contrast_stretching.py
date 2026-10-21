import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "img.jpg")
if not os.path.exists(image_path):
    image_path = os.path.join(script_dir, "images.jpg")
if not os.path.exists(image_path):
    image_path = "images.jpg"

image = Image.open(image_path).convert("RGB")
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

output_stretched_path = os.path.join(script_dir, "stretched_img.jpg")
Image.fromarray(stretched).save(output_stretched_path)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Contrast Stretched Image")
plt.imshow(stretched)
plt.axis("off")

plt.tight_layout()
output_plot_path = os.path.join(script_dir, "comparison_plot.png")
plt.savefig(output_plot_path, bbox_inches="tight")
plt.show()
