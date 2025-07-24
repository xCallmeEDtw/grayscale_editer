"""
Create an object responsible for handling the interaction between the GUI and images, e.g. opening/saving files, editing images according to the task requirements.
"""

from tkinter import *
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from doInput import *
from myPhoto import *
import copy
import os


def clearWindows(windows):
    """
    clean the  or windows
    """
    for widgets in windows.winfo_children():
        widgets.destroy()


def getOpenImgPath():
    """
    get a path of the open file by GUI
    """
    filetypes = (
        ("image", "*.jpg *.tif"),
        ('tif files', '*.tif'),
        ('jpg files', '*.jpg')
    )

    filepath = fd.askopenfilename(
        title='Open a file',
        initialdir='./TestImages',
        filetypes=filetypes)
    return(filepath)
def getSaveImgPath(defaultFile):
    """
    get a path of the save file by GUI
    """
    filepath = fd.asksaveasfilename(initialdir = "./TestImages", filetypes = [
        ("original type", defaultFile),
        ("jpg", ".jpg"),
        ("tif", ".tif"),
    ])
    if filepath != "" and ".jpg" not in filepath and ".tif" not in filepath :
        filepath += defaultFile   
    return filepath


class myCanv():        
    """
    a interactable GUI object canvas that store the image, 
    """
    def __init__(self, windows):
        """
        initial the canvas 
        """
        self.windows = windows

        self.canvas = None
        self.canvasHist= None
        
        self.indexOfHistory = -1
        self.History = []
        self.photo = None

    def update(self,undo=0):
        """
        update the canvas on the GUI
        """
        clearWindows(self.windows)
        self.canvas = Canvas(self.windows, width = self.photo.width , height = self.photo.height)
        self.canvas.pack(side="left",padx=100,expand= YES)
        self.canvas.create_image(0, 0, image=self.photo.imgtk, anchor=NW)

        self.canvasHist = FigureCanvasTkAgg(self.photo.histFigure, master=self.windows)
        self.canvasHist.draw()  
        self.canvasHist.get_tk_widget().pack(side="left")  
        
        if self.indexOfHistory == -1 :
            self.History.append(copy.copy(self.photo))
            self.indexOfHistory = 0

        elif undo == 1:
            pass
  
        else :
            self.indexOfHistory += 1
            self.History.insert(self.indexOfHistory ,copy.copy(self.photo))
           


    def OpenFile(self):
        """
        Change the image by the open path
        """
        path = getOpenImgPath()

        if not(os.path.isfile(path)): return
        self.photo = myPhoto(path)

        self.indexOfHistory = -1
        self.History = []
        self.update()

    def SaveFile(self):
        """
        save the image on origin file 
        """
        if self.indexOfHistory == -1 : return
        self.photo.saveFile()
        self.indexOfHistory = -1
        self.History = []
        self.update()
    def SaveAsFile(self):
        """
        save the image as a new file
        """
        if self.indexOfHistory == -1 : return
        path = getSaveImgPath(self.photo.path[self.photo.path.rfind('.'):])
        if path == "": return
        #print(path)
        self.photo.path = path
        self.SaveFile()

    def doLinear(self):
        """
        open a entry box,and let user input a,b
        do lineary change(img=a*img0+b) to the image on canvas
        """
        entry = myEntry(self.windows,2,["a","b"],[1,0],float)
        self.windows.wait_window(entry.inputWindow)
        try:
            a,b = map(float,entry.getEntered())
            self.photo.doLinearlyConstrast(a,b)
            self.update()
        except: 
            pass
    def doExp(self):
        """
        open a entry box,and let user input a,b
        do exponential change(img=exp(a*img0+b)) to the image on canvas
        """        
        entry = myEntry(self.windows,2,["a","b"],[1,0],float)
        self.windows.wait_window(entry.inputWindow)
        try:
            a,b = map(float,entry.getEntered())
            self.photo.doExpConstrast(a,b)
            self.update()
        except: 
            pass
    def doLog(self):
        """
        open a entry box,and let user input a,b
        do logarithmic change(img=log(a*img0+b)) to the image on canvas
        """        
        entry = myEntry(self.windows,2,["a","b"],[1,0],float)
        self.windows.wait_window(entry.inputWindow)
        try:
            a,b = map(float,entry.getEntered())
            self.photo.doLogConstrast(a,b)
            self.update()
        except: 
            pass
    def undo(self):
        """
        undo the image on canvas 
        """            
        if self.indexOfHistory <= 0:
            return
        self.indexOfHistory -= 1
        self.photo = copy.copy(self.History[self.indexOfHistory])
        self.update(undo=True)

    def resize(self):
        """
        make a entry make user input a percentage p(%)
        resize the image on canvas by p
        """
        entry = myEntry(self.windows,1,["percentage(%)"],[100],int)
        self.windows.wait_window(entry.inputWindow)
        try:
            s, = map(int,entry.getEntered())
            self.photo.doResize(s)
            self.update()
        except: 
            pass
    def rotate(self):
        """
        make a entry make user input a degree deg
        rotate the image on canvas by the degree deg
        """
        entry = myEntry(self.windows,1,["degree"],[0],float)
        self.windows.wait_window(entry.inputWindow)
        try:
            degree, = map(float,entry.getEntered())
            self.photo.doRotate(degree)
            self.update()
        except: 
            pass
    def sliceGrayLV(self):
        """
        make a entry make user input lower bound and upper bound, and a checkbox to check if the gray level be reserved
        and do gray level slicing
        """
        try:

            entry = myEntry(self.windows,2,["lower bound","upper bound"],[0,255],onlyType=float,hasCheckBox=1,checkBoxLabel="preserve?")
            self.windows.wait_window(entry.inputWindow)
            if entry.isCancel: return
            minValue,maxValue = map(float,entry.getEntered())
            self.photo.doGrayLV(minValue,maxValue,to_preserve=entry.checkState.get())
            self.update() 
        except:
            pass 
    def autolevl(self):
        """
        auto-level the image on canvas
        """
        try:
            self.photo.doAutolevel()
            self.update()  
        except:
            pass 
    def bit_plane(self):
        """
        make a spinbox let user input 1-7 to n
        get the bit-plane image of n on canvas
        """
        spinbox = mySpinbox(self.windows,"bit-plane (0-7)",(0,7))
        self.windows.wait_window(spinbox.inputWindow)

        try:
            if spinbox.isCancel: return
            self.photo.doBitplane(spinbox.entered)
            self.update() 
        except:
            pass   
    def sharp(self):
        """
        make a scale s that user choose 1-10
        sharpen the image by the degree s on canvas
        """
        scale = myScale(self.windows,"scale (1-10)",(1,10))
        self.windows.wait_window(scale.inputWindow)
        try:
            if scale.isCancel: return
            self.photo.doSharp(scale.entered)
            self.update()
        except:
            pass
    def smooth(self):
        """
        make a scale s that user choose 1-10
        do smooth of the image by the degree s on canvas
        """
        scale = myScale(self.windows,"scale (1-10)",(1,10))
        self.windows.wait_window(scale.inputWindow)
        try:
            if scale.isCancel: return
            self.photo.doSmooth(2*scale.entered+1)
            self.update()
        except:
            pass
