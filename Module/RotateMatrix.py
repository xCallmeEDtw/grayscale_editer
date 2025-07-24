from numpy import *
import numpy as np
from math import *
from functools import reduce 

def RotateMatrix(M,deg):
	"""
	rotate the matrix M troughout matrix muiltiplication 

	P0/Term is to transform the matrix with the form [ [x],[y],[1],[M[x][y]].... ]

	the "1" in the third row is for matrix calculation

	for instance 
	1 4 7      0 1 2 0 1 2 0 1 2
	2 5 7 -->  0 0 0 1 1 1 2 2 2
	3 6 9	   1 1 1 1 1 1 1 1 1
		       1 2 3 4 5 6 7 8 9

	A is a translation Matrix to shift the the middle position of M as (0,0)
	1 0 -a 0
	0 1 -b 0
	0 0  1 0
	0 0  0 1

	B is a rotation matrix to rotate M with degree deg
	 cos(deg) sin(deg) 0 0
	-sin(deg) cos(deg) 0 0
	        0       0  1 0
			0       0  0 1
			
	C is a scailing Matix with the scale S, which let the img in the frame 
	n 0 0 0 
	0 n 0 0
	0 0 1 0
	0 0 0 1

	D is a translation Matrix to shift the position back to middle
	1 0 a 0
	0 1 b 0
	0 0 1 0
	0 0 0 1

	P = D*C*B*A*P0 
	and rotateM is the matrix transform from P
	"""

	newHeight, newWeight = M.shape
	rotateM = zeros([newHeight+1,newWeight+1]).astype(uint8)
	Terms = [[],[],[],[]]
	corner = [[],[],[],[]]
	DegSin = lambda x: sin(radians(x))
	DegCos = lambda x: cos(radians(x))
	distanceX = lambda A:   max (A[:1 ,:][0]) - min((A[:1 ,:][0]))
	distanceY = lambda A:   max (A[1:2 ,:][0]) - min((A[1:2 ,:][0]))

	#transform matrix into terms
	for i in range(M.shape[0]):
		for j in range(M.shape[1]):
			#if M[i][j] != 0:
			Terms[0].append(i)
			Terms[1].append(j)
			Terms[2].append(1)
			Terms[3].append( M[i][j])
			if i in [0,M.shape[0]-1] and j in [0,M.shape[1]-1]:
				corner[0].append(i)
				corner[1].append(j)
				corner[2].append(1)
				corner[3].append( M[i][j])	
	corner = array(corner) #corner is a terms store the 4 corners of matrix
	P0 = array(Terms)


	#create A,B,C,D matix as the definition above
	A = array([[1,0,-1*M.shape[0]/2,0],[0,1,-1*M.shape[1]/2,0],[0,0,1,0],[0,0,0,1]])
	B = array([[DegCos(deg),DegSin(deg),0,0],[-1*DegSin(deg),DegCos(deg),0,0],[0,0,1,0],[0,0,0,1]])
	D = array([[1,0,1*M.shape[0]/2,0],[0,1,1*M.shape[1]/2,0],[0,0,1,0],[0,0,0,1]])
	cornerRotate = reduce(matmul,[D,B,A,corner])
	S=min(distanceX(corner)/distanceX(cornerRotate), distanceY(corner)/distanceY(cornerRotate)) #count the size after rotaing
	C = array([[S,0,0,0],[0,S,0,0],[0,0,1,0],[0,0,0,1]]) 

	P = reduce(matmul,[D,C,B,A,P0]).astype(int) # do the matrix mutiplication D*C*B*A*P0

	#transform the terms back to matrix
	for k in range(len(P[0])):
		i = P[0][k]
		j = P[1][k]
		val = P[3][k]

		rotateM[i][j] = val
		
	return rotateM[:-1,:-1]

