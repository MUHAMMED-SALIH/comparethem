# USAGE
# python compare.py

# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import sys
import PIL
from PIL import Image
import urllib
import math


sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float"))**2)
	err =(err/ float(imageA.shape[0] * imageA.shape[1]))
	
	err=math.sqrt(err)
	
	if err>100:
		err=100
	
	return 100-err
		

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	

	# setup the figure
	fig = plt.figure(title)
	
	
	plt.suptitle(" \nSIMILARITY: %.2f percentage" % (m))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

 
imagea=raw_input("enter the url of the first image\n")
urllib.urlretrieve(imagea,"a.jpg")
img = Image.open('a.jpg')

img = img.resize((300,300), PIL.Image.ANTIALIAS)
img.save('d.jpg')

imageb=raw_input("\nenter the url of the second image \n")
urllib.urlretrieve(imageb, "k.jpg")
img = Image.open('k.jpg')


img = img.resize((300,300), PIL.Image.ANTIALIAS)
img.save('f.jpg')
original = cv2.imread("d.jpg")
contrast = cv2.imread("f.jpg")




 
 	



# convert the images to grayscale
img1 = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("first image", img1), ("second image", img2)

# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

#compare images
compare_images(img1, img2, "first image vs.second image")

