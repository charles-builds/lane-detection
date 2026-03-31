# Lane Detection using OpenCV and Python

## What This Project Does
This project detects lane lines on roads using computer vision.
It is the basic technology used in self-driving cars like Tesla.

## How It Works
1. Read a road image
2. Convert to grayscale
3. Detect edges using Canny algorithm
4. Mask the road area
5. Detect lane lines using Hough Transform
6. Draw blue lines on detected lanes

## Technologies Used
- Python
- OpenCV
- NumPy

## Result
The program shows 4 windows:
- Original image
- Edge detection
- Road area mask
- Final result with detected lanes
