# 'patches' in 'matplotlib' is used for implementing shapes
from  matplotlib import patches as shape
import matplotlib.pyplot as plt

#mtcnn is the algorithm for detection(Convolution Neural Network)
# import mtcnn as CNN
from mtcnn.mtcnn import MTCNN

import glob
from PIL import Image
import datetime

import os
import time

# Imports folder file path from the image.py file
from image import file_path

# Prepare image folder before bounding box detection 
def data_preparation():

	# Iterates through all images
	file_list = [image for image in glob.glob(file_path + "/*.jpg")]

	for x in file_list:
		image = Image.open(x,"r")
		image = x

		
		#Assigns the algorithm and facial detection to the selected image
		detectFace = MTCNN().detect_faces(plt.imread(image))

		# Images with no face deteced will be deleted
		if len(detectFace) == 0:
			os.remove(image)

	
data_preparation()

# Start timing the detection time
start = time.time()

def recognition():


	# Reads the same folder now it's prepared 
	file_list = [image for image in glob.glob(file_path + "/*.jpg")]

	for x in file_list:
		image = Image.open(x,"r")
		image = x

		#Assigns the algorithm and facial detection to the images
		people = MTCNN().detect_faces(plt.imread(image))	

		# #This function handles detecting and drawing boxes around faces
		plt.imshow(plt.imread(image))
		
		# #For loop that draws the boxes and dots on recognised faces
		for i in people:
				
			#X, Y axis & Width, Height for box
			X, Y, W, H = i['box']

			axis = X,Y

			#Features of box
			box = shape.Rectangle((axis), W, H, 
			color = 'red',
			linestyle = 'dashed',
			fill=False)
				
			#matplotlib finds the axis
			apply = plt.gca().add_patch

			#This displays the box around the faces
			apply(box)
		
		# Saves each image as the exact date and time
		plt.savefig(f'detected/images{datetime.datetime.now()}.jpg', dpi = 300)
		

		plt.close()

# Error catch for any error within the program
try:
	recognition()
except Exception:
	print("An Error has occured")

# Ends time counting after all images are detected
end = time.time()
		
print(end - start)	

