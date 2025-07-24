"""
Spin a matrix 90,180,270 degree
"""
from numpy import *
import numpy as np
import cv2   

def Spin270(M):
	"""
	Spin a matrix 270 degree

	Term is to transform the matrix with the form [ [x],[y],[M[x][y]].... ]
	
	and we can switch the terms x,y to do spin the matix

	for instance 
	1 4 7      0 1 2 0 1 2 0 1 2       0 0 0 1 1 1 2 2 2      1 2 3
	2 5 7 -->  0 0 0 1 1 1 2 2 2 --->  0 1 2 0 1 2 0 1 2 -->  4 5 6 
	3 6 9      1 2 3 4 5 6 7 8 9       1 2 3 4 5 6 7 8 9      7 8 9
	"""
	newWeight,newHeight = M.shape
	spinM = zeros([newHeight,newWeight]).astype(uint8)
	Terms = [[],[],[]]

	#transform matrix into Terms
	for yi in range(M.shape[1]):
		for xi in range(M.shape[0]):
			Terms[0].append(xi)
			Terms[1].append(yi)
			Terms[2].append(M[xi][yi])
	Terms =array( Terms)
	rotateTerms = Terms.copy()

	rotateTerms[:2:,:] = Terms[1::-1,:] #flip the terms

	#transform Terms back into matrix 
	for k in range(len(rotateTerms[0])):
		xi = rotateTerms[0][k]
		yi = rotateTerms[1][k]
		
		spinM[xi][yi] = rotateTerms[2][k]


	return spinM


def Spin90(M):
	"""
	Spin a matrix 90 degree
	"""
	return  Spin270(M)[::,::-1] #flip the matrix that turned 270 degree
def Spin180(M):
	"""
	Flip a matrix 
	"""
	return M[::-1,::] #flip the matrix 




