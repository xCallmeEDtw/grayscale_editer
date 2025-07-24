"""
Create three objects to implement an input window, Spinbox window, and scaling window, respectively.
"""
from tkinter import *
from functools import partial
def on_validate_float(entry,try2input):
    """
    check if try2input is float
    """
    ctx = entry.get()
    if len(try2input) < len(ctx):
        return True
    inputChr = try2input
    for c in ctx :
    	inputChr = inputChr.replace(c,"",1)
    if inputChr.isdigit():
        return True
   
    if inputChr == "." and "." not in ctx and try2input != ".":
        return True
    if inputChr == "-" and "-" not in ctx and try2input[0] == "-":
        return True
    return False
def on_valildate_int(try2input):
	"""
	check if try2input is int
	"""
	if try2input.isdigit():
		return True
	return False
class myEntry():
	def __init__(self, windows, totalNums, labelTexts,initVal,onlyType=0,hasCheckBox=0,checkBoxLabel=""):
		"""
		create a entry box
		totalNums is the numbers of total inputs
		labelTexts is the label of each entry
		initVal is the initial value of the entry
		onlyType is to lock the type of tnry
		if hasCheckBox is 1, the entry will has a check box with the label checkBoxLabel
		"""
		self.totalNums = totalNums
		self.windows = windows
		self.initVal = initVal
		self.inputWindow = Toplevel(windows)
		self.inputWindow.geometry('450x250')
		self.entered = [None]*totalNums
		self.labels = [None]*totalNums
		self.entries = [None]*totalNums
		self.hasCheckBox = hasCheckBox
		self.isCancel = 1
		for i in range(self.totalNums):
			self.labels[i] = Label(self.inputWindow, text=labelTexts[i] )
			self.entries[i] = Entry(self.inputWindow)
			self.entries[i].insert(END,str(self.initVal[i]))
			self.labels[i].pack()
			self.entries[i].pack()
			if onlyType == float:
				validate_float = partial(on_validate_float,self.entries[i])
				self.entries[i].config(validate="key", validatecommand=(self.windows.register(validate_float), "%P"))
			if onlyType == int:
				self.entries[i].config(validate="key", validatecommand=(self.windows.register(on_valildate_int), "%S"))
			self.entries[i].bind("<FocusIn>", self.on_entry_focus_in)
		if hasCheckBox:
			self.checkState = IntVar()
			self.myCheck = Checkbutton(self.inputWindow,variable=self.checkState,text=checkBoxLabel)
			self.myCheck.pack()
		btnConfirm = Button(self.inputWindow, text="confirm",command= lambda:self.__confirm())
		btnConfirm.pack()
		btnCancel = Button(self.inputWindow, text="cancel",command= lambda:self.__cancel())
		btnCancel.pack()
		

	def getEntered(self):
		return self.entered

	def __confirm(self):
		self.isCancel = 0
		for i in range(self.totalNums):
			self.entered[i] = self.entries[i].get()
		if not(all(self.entered)): 
			return
		self.inputWindow.destroy()
	def __cancel(self):
		self.inputWindow.destroy()
	def on_entry_focus_in(self,event):
	    current_entry = event.widget
	    for i in range(self.totalNums):
	        if self.entries[i] != current_entry:
	        	if self.entries[i].get() == "":
	        		self.entries[i].insert(END,str(self.initVal[i]))


class mySpinbox():
	def __init__(self,windows,labelText,range):
		"""
		create a spin box
		labelText is the label of spinbox
		range is the range of spin box
		"""
		self.windows = windows
		self.entered =0 
		self.isCancel = 1
		self.inputWindow = Toplevel(windows)
		self.inputWindow.geometry('450x250')
		self.label = Label(self.inputWindow, text=labelText)
		self.label.pack()
		self.spinbox = Spinbox(self.inputWindow,from_=range[0], to=range[1], width=5, state=NORMAL)
		self.spinbox.pack()
		self.spinbox.config(validate="key", validatecommand=(self.windows.register(on_valildate_int), "%S"))

		btnConfirm = Button(self.inputWindow, text="confirm",command= lambda:self.__confirm())
		btnConfirm.pack()
		btnCancel = Button(self.inputWindow, text="cancel",command= lambda:self.__cancel())
		btnCancel.pack()
	def __confirm(self):
		self.isCancel =0 
		self.entered = int(self.spinbox.get())
		self.inputWindow.destroy()
	def __cancel(self):
		self.inputWindow.destroy()
class myScale():
	def __init__(self,windows,labelText,range):
		"""
		create a scale
		labelText is the label of scale
		range is the range of scale
		"""
		self.windows = windows
		self.entered =0 
		self.isCancel = 1
		self.inputWindow = Toplevel(windows)
		self.inputWindow.geometry('450x250')
		self.label = Label(self.inputWindow, text=labelText)
		self.label.pack()

		self.scale = Scale(self.inputWindow,from_=range[0], to=range[1], orient=HORIZONTAL, length=200)
		self.scale.pack()
		btnConfirm = Button(self.inputWindow, text="confirm",command= lambda:self.__confirm())
		btnConfirm.pack()
		btnCancel = Button(self.inputWindow, text="cancel",command= lambda:self.__cancel())
		btnCancel.pack()
	def __confirm(self):
		self.isCancel =0 
		self.entered = int(self.scale.get())
		self.inputWindow.destroy()
	def __cancel(self):
		self.inputWindow.destroy()