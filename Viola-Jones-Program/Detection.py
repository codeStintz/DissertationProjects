#Importing'OpenCV2' which is python library for computer vision
import cv2
# from image import file_path
import os
from PIL import Image
import datetime
import glob
import time

# Imports folder file path from the image.py file
from image import file_path

# Prepare image folder before bounding box detection 
def data_preparation():

	# Iterates through chosen folder
	file_list = [image for image in glob.glob(file_path + "/*.jpg")]
	# Reads each image within the folder
	for x in file_list:
		image = Image.open(x,"r")
		image = cv2.imread(x)

		#Converts the image to grayscale which is required for the Haar Algorithm
		gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		#DetectMultiScale handles detection within images and the different specifications for detection
		detectFace = cv2.CascadeClassifier(
			'viola-jones-haar-algorithm.xml').detectMultiScale(gray_img, 1.3, 3)

		# If no faces are detected, deletes the image
		if len(detectFace) == 0:
			os.remove(x)
			
data_preparation()

# Start timing detection process
start = time.time()


def recognition():

	# Reads the same folder again now its prepared
	file_list = [image for image in glob.glob(file_path + "/*.jpg")]
	for x in file_list:
		image = Image.open(x,"r")
		image = cv2.imread(x)

		gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	
		#DetectMultiScale handles detection within images and the different specifications for detection
		detectFace = cv2.CascadeClassifier('viola-jones-haar-algorithm.xml').detectMultiScale(gray_img, 1.3, 3)
	
		#This code is responsible for the box around a persons face and eyes
		def detect(face):

			for i in face:
				
				#X, Y axis & Width, Height
				x, y, width, height = i
				
				#Calculating the measurements
				X = x + width
				Y = y + height

				#Line axis for the box
				axis = (x,y),(X,Y)

				colour = (0,0,250) #red

				#Puts all the attributes of the box together
				cv2.rectangle(image, axis[0],axis[1],
				colour,
				thickness=2)

			return
		
		detect(detectFace)
		
		# Displays the image with facial recognition
		cv2.imshow('Haar Facial Detection', image)
		
		# Saves the detected face
		cv2.imwrite(f'detected/images{datetime.datetime.now()}.jpg', image)


recognition()

# Ends the detection timing
end = time.time()
		
print(end - start)