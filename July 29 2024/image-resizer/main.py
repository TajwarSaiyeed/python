import cv2
import os

os.environ["XDG_SESSION_TYPE"] = "xcb"

image = cv2.imread('tajwar.jpg')
resize_image = cv2.resize(image, (200, 200))

cv2.imshow('Tajwar', resize_image)

cv2.waitKey(0)
