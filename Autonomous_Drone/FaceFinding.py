# Importing 'OpenCV2' which is python library for computer vision
import cv2

def locate(picture):
    #Loads the chosen algorithm used
    algorithm = cv2.CascadeClassifier("viola-jones-haar-algorithm.xml")
    # Converts the image to black and white which is required for the viola-jones algorithm
    image = algorithm.detectMultiScale(cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY), 1.2, 8)

    # centre point and area of detected faces
    centrePoint = []
    peopleArea = []
    
    # Draws a red rectangle around the detected user face
    for i in image:

        # axies, width and heigh of detected face
        x_axis, y_axis, width, height = i

        # Equations to find centre point and area of detected face
        centrePoint.append([x_axis + width // 2, y_axis + height // 2])
        peopleArea.append(width * height)

    #States the largest face is the face to be detected, tracked, and visually detected
    if len(peopleArea) > 0:
        maximum = max(peopleArea)
        i = peopleArea.index(maximum)
        cv2.rectangle(picture, (x_axis, y_axis), (x_axis + width, y_axis + height), (0, 0, 255), 1)
        return picture, [centrePoint[i], peopleArea[i]]
    else:
        return picture, [[0, 0], 0]