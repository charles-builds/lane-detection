import cv2


image = cv2.imread('road.jpg')


if image is None:
    print("ERROR: road.jpg not found!")
    print("Make sure road.jpg is in the same folder as this file")
else:
    print("Image loaded successfully!")
    cv2.imshow('My Road Image', image)
    cv2.waitKey(0)