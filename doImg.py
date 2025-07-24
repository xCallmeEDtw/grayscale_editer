from numpy import * 
import cv2                                                                             
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from operator import add 
from Module.RotateMatrix import *
from Module.ResizeMatrix import *
from Module.SpinMatrix import *

def resizeIMG(img,theSize=100):
	"""
	do the resize of img with the percentage of theSize

	and called ResizeMatrix in Module.ResizeMatrix
	"""
	theSize /= 100
	return ResizeMatrix(img,theSize) #function in Module.ResizeMatrix

def linearlyConstrast(img,a=1,b=0 ):
	"""
	do linearly Constrast of the image by let img = img0*a + b
	"""
	img2 = (img.astype(float64))
	img2 = img*a + b #linearly Constrast
	return clip(img2,0,255).astype(uint8)
def expConstrast(img,a=1,b=0):
	"""
	do exponentially Constrast of the image by let img = exp(img0*a + b)
	"""
	img2 = (img.astype(float64))
	img2 = img*a + b
	img3 = (exp(img2.astype(float64)) ) #exponentially Constrast
	return clip(img3,0,255).astype(uint8)
def logConstrast(img,a=1,b=0):
	"""
	do logarithmically Constrast of the img by let img = log(img0*a + b)
	"""
	img2 = (img.astype(float64))
	img2 = img*a + abs(b)
	img4 = log(img2+1) #logarithmically Constrast
	return clip(img4,0,255).astype(uint8)
def imgRotate(img,degree):
	"""
	do img rotate by degree
	if the degree is 90k, then call function in Module.SpinMatrix
	else call function RotateMatrix in Module.RotateMatrix
	"""
	if degree % 360 == 0: return img
	
	if degree % 90 == 0:
		degree %= 360
		if degree % 180 == 0: return Spin180(img)
		if degree % 270 == 0: return Spin270(img)
		Spin90(img)#function in Module.SpinMatrix

	return RotateMatrix(img,degree)#function in Module.RotateMatrix


def grayLevelSlicing(img, theMin, theMax, keepDefalut=False):
	"""
	do gray level slicing of img, by the range theMin-theMax
	if keepDefault = True , preserve the origin value
	"""
	img2 = img.copy()
	for i in range(img2.shape[0]):
		for j in range(img2.shape[1]):
			if theMax >= img2[i][j] >= theMin: #check if img2[i][j] is in the range of slicing 
					img2[i][j]= 255
			else:
				if (keepDefalut==False): #if user do not want preserve, then set value to black
					img2[i][j] = 0
	return img2


def myHistogram(img):
	"""
	get the histogram of img
	"""
	f = Figure(figsize=(5,4), dpi=100)
	p = f.gca()
	p.hist(img.ravel(),256,[0,256])
	return(f)

def imgAutolevel(img):
	"""
	do auto level by call the Histogram equalization in openCV
	"""
	return cv2.equalizeHist(img)
def nbitPlane(img,numOfPlane):
	"""
	get the numOfPlane bit-Plane of img
	"""
	Planes = zeros(img.shape).astype(uint8)

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if f"{img[i][j]:08b}"[7-numOfPlane] == '1':  #change img[i][j] to binery number and check the n bits is "1" 
				Planes[i][j] = 255
	return Planes

def ImgSmooth(img,n=3):
	"""
	do img smoothing by average filter n*n
	"""
	kones = ones((n,n))*1/(n**2) # make a average filter with the size n*n
	blur = doFilter(img,kones) #call the filter function written below
	return blur.clip(0,255).astype(uint8)

def getLaplacian(n=3):
	"""
	get the Laplacian filter of n
	"""
	kernel = 	array([[0, 1, 0],
	                   [1, -4, 1],
	                   [0, 1, 0]])
	return kernel
def ImgSharp(img,k=1):
	"""
	do img sharpen by Laplacian filter
	first get an blur filtered by Laplacian
	and add the blur back to the origin img with a coefficent k
	"""
	img2 = img.copy().astype(float64)
	blur = doFilter(img2,getLaplacian()).astype(float64) #call the filter function written below
	k = (k+2)/6 # do a linear adjustment that map from (1,10) to (0.5,2) e.g. 5 --> 1
	img2 = img2 + (-1)*k*blur # add the filter with the weighted k
	return img2.clip(0,255).astype(uint8)
def doFilter(img,kernel):
	"""
	put the filter(kernel) on the img
	"""
	n = kernel.shape[0]
	borderSpace =  n//2  #space for padding
	heightRange = (borderSpace,borderSpace+img.shape[0]) #the height range without the padding
	weightRange = (borderSpace,borderSpace+img.shape[1]) #the weight range without the padding
	valueSlice = slice(*heightRange),slice(*weightRange) #slice the padding
	blur = zeros([*map(add,img.shape, [borderSpace*2]*2)],dtype=float64) 

	blur[valueSlice] = img.copy().astype(float64)
	tmp = blur.copy()

	#do the filter
	for i in range(*heightRange): 
		for j in range(*weightRange):
			blur[i][j] = sum(kernel* tmp[i-borderSpace:i-borderSpace+n, j-borderSpace:j-borderSpace+n ])
	blur = blur[valueSlice] #slice the padding 

	return blur 	



if __name__ == '__main__':
	"""
	this is for testing
	"""
	path = r'C:/Users/edward/Desktop/coding-u/dip/B112040003_張景旭_HW1/TestImages/woman.tif'
	pathout = r'C:/Users/edward/Desktop/coding-u/dip/B112040003_張景旭_HW1/Test.jpg'
	imgg = cv2.imdecode(fromfile(path,dtype=uint8),cv2.IMREAD_GRAYSCALE)
	imgg2 = imgRotate(imgg,80)
	cv2.imshow('img',imgg2)
	cv2.waitKey(0)
