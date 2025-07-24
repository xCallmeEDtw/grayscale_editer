from numpy import *
import numpy as np


def ResizeMatrix(M,n): 
	"""
	resize the matrix M troughout matrix muiltiplication and do bilinear interpolation

	Term is to transform the matrix with the form [ [x],[y],[M[x][y]].... ]

	for instance 
	1 4 7      0 1 2 0 1 2 0 1 2
	2 5 7 -->  0 0 0 1 1 1 2 2 2
	3 6 9      1 2 3 4 5 6 7 8 9

	B is a scailing Matix with the scale n
	n 0 0
	0 n 0 
	0 0 1
	resizeTerm = B*Term 
	and resizeM is the matrix transform from resizeTerm
	"""
	newHeight, newWeight = map(round,map(multiply,M.shape,[n]*2))
	resizeM = zeros([newHeight+1,newWeight+1]).astype(uint8)
	Terms = [[],[],[]]

 	#transform matrix into terms
	for yi in range(M.shape[1]):
		for xi in range(M.shape[0]):
			Terms[0].append(xi)
			Terms[1].append(yi)
			Terms[2].append(M[xi][yi])
	B = array([[n,0,0],[0,n,0],[0,0,1]])
	Terms = array(Terms)

	resizeTerms = matmul(B,Terms).astype(int) #matrix mutiplcation

	#transform terms back to matrix
	for k in range(len(resizeTerms[0])):
		i = resizeTerms[0][k]
		j = resizeTerms[1][k]
		val = resizeTerms[2][k]

		
		resizeM[i][j] = val

	#bilinear interpolation
	for k in range(len(resizeTerms[0])-M.shape[0]-1):
	
		X0,Y0,Vx0y0 = resizeTerms[:,k]
		Vx0y1 = resizeTerms[:,k+1][2]
		X1,Y1,Vx1y1 = resizeTerms[:,k+M.shape[0]+1]
		Vx1y0 = resizeTerms[:,k+M.shape[0]][2]
		if X1<X0 or Y1<Y0: continue
		
		for x in range(X0,X1+1):
			for y in range(Y0,Y1+1):
				if x in [X0,X1] and y in [Y0,Y1]: continue
				

				l = (x-X0)/(X1-X0)
				u = (y-Y0)/(Y1-Y0)
				resizeM[x][y] = l*u*Vx1y1 + l*(1-u)*Vx1y0+ (1-l)*u*Vx0y1 + (1-l)*(1-u)*Vx0y0 #the formula of bilinear interpolation
	return resizeM[:-1,:-1]
