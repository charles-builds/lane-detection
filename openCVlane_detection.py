import cv2
import numpy as np

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    polygons = np.array([
        [(0, height),
         (width, height),
         (width//2, height//2)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2),
                    (255, 0, 0), 10)
    return line_image


image = cv2.imread('road.jpg')

if image is None:
    print("ERROR: road.jpg not found!")
else:
    copy = np.copy(image)
    canny_image = canny(copy)
    cropped = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(
        cropped, 2, np.pi/180, 100,
        np.array([]),
        minLineLength=40,
        maxLineGap=5
    )
    line_image = display_lines(copy, lines)
    combo = cv2.addWeighted(copy, 0.8, line_image, 1, 1)

    cv2.imshow('1 - Original', image)
    cv2.imshow('2 - Edges', canny_image)
    cv2.imshow('3 - Road Area', cropped)
    cv2.imshow('4 - Final Result', combo)
    cv2.waitKey(0)
