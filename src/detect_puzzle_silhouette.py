#!/usr/bin/env python
# coding: utf-8

# In[53]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# In[ ]:


# Beispielbild laden
image_path = "../data/pzl_3_processed/pzl_3_full_front.jpg"  # Ersetze durch den tatsächlichen Pfad
image = cv2.imread(image_path)
if image is None:
    print(f"Fehler beim Laden des Bildes: {image_path}")
else:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Originalbild")
    plt.axis("off")
    plt.show()


# In[55]:


## Wandle das Bild in Graustufen um ohne die OpenCV-Funktion cvtColor zu verwenden
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
# Konvertiere das Graustufenbild in uint8
gray_image = np.clip(gray_image, 0, 255).astype(np.uint8)
# Zeige das Graustufenbild an
plt.imshow(gray_image, cmap='gray')
plt.title("Graustufenbild")
plt.axis("off")
plt.show()


# ### Kantenerkennung mithilfe vom Sobel-Operator

# In[56]:


#Erkenne mithilfe vom Sobel-Operator 
#Kanten im Graustufenbild 
#ohne die OpenCV-Funktion Sobel zu verwenden

def sobel_operator(image):
    # Sobel-Kernel für x- und y-Richtung
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1,-2,-1]])

    # Initialisiere das Ergebnisbild
    gradient_magnitude = np.zeros_like(image)

    # Wende den Sobel-Operator an
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            gx = np.sum(sobel_x * image[i-1:i+2, j-1:j+2])
            gy = np.sum(sobel_y * image[i-1:i+2, j-1:j+2])
            gradient_magnitude[i, j] = np.sqrt(gx**2 + gy**2)

    return gradient_magnitude
# Wende den Sobel-Operator auf das Graustufenbild an
edges = sobel_operator(gray_image)
# Normalisiere die Kantenstärke auf den Bereich [0, 255]
edges = np.clip(edges, 0, 255).astype(np.uint8)
# Zeige das Ergebnis an
plt.imshow(edges, cmap='gray')


# ### Kantenerkennung mithilfe von Canny-Kantendetektion

# In[58]:


# Kantenerkennung mithilfe von Canny-Kantendetektion ohne die OpenCV-Funktion Canny zu verwenden
def canny_edge_detection(image, low_threshold, high_threshold):
    # Wende den Sobel-Operator an
    gradient_magnitude = sobel_operator(image)

    # Non-maximum Suppression
    suppressed = np.zeros_like(gradient_magnitude)
    angle = np.arctan2(np.gradient(image, axis=0), np.gradient(image, axis=1)) * 180 / np.pi
    angle[angle < 0] += 180

    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            q = 255
            r = 255

            # Winkel anpassen
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = gradient_magnitude[i, j + 1]
                r = gradient_magnitude[i, j - 1]
            elif (22.5 <= angle[i, j] < 67.5):
                q = gradient_magnitude[i + 1, j - 1]
                r = gradient_magnitude[i - 1, j + 1]
            elif (67.5 <= angle[i, j] < 112.5):
                q = gradient_magnitude[i + 1, j]
                r = gradient_magnitude[i - 1, j]
            elif (112.5 <= angle[i, j] < 157.5):
                q = gradient_magnitude[i - 1, j - 1]
                r = gradient_magnitude[i + 1, j + 1]

            if (gradient_magnitude[i, j] >= q) and (gradient_magnitude[i, j] >= r):
                suppressed[i, j] = gradient_magnitude[i, j]
            else:
                suppressed[i, j] = 0

    # Double Thresholding
    strong_edges = (suppressed >= high_threshold)
    weak_edges = ((suppressed >= low_threshold) & (suppressed < high_threshold))

    # Edge Tracking by Hysteresis
    edges_final = np.zeros_like(suppressed)
    edges_final[strong_edges] = 255

    for i in range(1, suppressed.shape[0] - 1):
        if weak_edges[i, j]:
            if ((strong_edges[i + 1, j - 1] or strong_edges[i + 1, j] or strong_edges[i + 1, j + 1]) or
                (strong_edges[i, j - 1] or strong_edges[i, j + 1]) or
                (strong_edges[i - 1, j - 1] or strong_edges[i - 1, j] or strong_edges[i - 1, j + 1])):
                edges_final[i, j] = 255
    return edges_final
# Wende die Canny-Kantendetektion an
#high_treshold = 65 bei einzelnem Puzzle

edges_canny = canny_edge_detection(gray_image, low_threshold=100, high_threshold=65)
# Zeige das Ergebnis der Canny-Kantendetektion an
plt.imshow(edges_canny, cmap='gray')
plt.title("Canny-Kantendetektion")
plt.axis("off")
plt.show()

