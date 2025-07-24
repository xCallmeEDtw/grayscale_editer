import cv2  
import PIL.Image, PIL.ImageTk
from doImg import *
from numpy import *
class myPhoto():
    """
    this is a class that store the img and the histgram
    and implement the method to the function in doImg.py 
    """
    def __init__(self, path):
        """
        give the path to the myPhoto and initial the myPhoto
        """
        self.path = path
        self.img = cv2.imdecode(fromfile(path,dtype=uint8),cv2.IMREAD_GRAYSCALE)
        self.update()
    def update(self):
        """
        update the photo by the path
        """
        self.height, self.width = self.img.shape
        self.imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.img))
        self.histFigure = myHistogram(self.img)

    def saveFile(self):
       filetype = self.path[self.path.rfind('.'):]
       cv2.imencode(filetype,self.img)[1].tofile(self.path)
     
    def doLinearlyConstrast(self,a,b):
        self.img = linearlyConstrast(self.img,a,b)
        self.update()
    def doExpConstrast(self,a,b):
        self.img = expConstrast(self.img,a,b)
        self.update()
    def doLogConstrast(self,a,b):
        self.img = logConstrast(self.img,a,b)
        self.update()
    def doResize(self,s):
        self.img = resizeIMG(self.img,theSize=s)
        self.update()
    def doRotate(self,degree):
        self.img = imgRotate(self.img,degree)
        self.update()
    def doGrayLV(self,minValue,maxValue,to_preserve=False):
        self.img = grayLevelSlicing(self.img, minValue, maxValue, keepDefalut=to_preserve)
        self.update()
    def doAutolevel(self):
        self.img = imgAutolevel(self.img)
        self.update()
    def doBitplane(self,n):
        self.img = nbitPlane(self.img,n)
        self.update()
    def doSharp(self,n):
        self.img = ImgSharp(self.img,n)
        self.update()
    def doSmooth(self,n):
        self.img = ImgSmooth(self.img,n)
        self.update()