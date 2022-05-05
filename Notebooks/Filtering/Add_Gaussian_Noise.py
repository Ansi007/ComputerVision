import numpy as np
import cv2 


#   Image reading as grayscale
img = cv2.imread('book.png', 0)


#   Specifying Gaussian mean and std
mean = 0.0   # some constant
std = 15.0    # some constant (standard deviation)


noisy_img = img + np.random.normal(mean, std, img.shape)
noisy_img_clipped = np.clip(noisy_img, 0, 255)  # we might get out of bounds due to noise

cv2.imwrite('noisy_book.png', noisy_img_clipped)