"""
DIP hw1
author: b112040003 張景旭
"""

from doGui import *
if __name__ == '__main__':
    root = Tk()
    root.title("hw1")
    root.geometry('1920x1080')


    frame = Frame(root)
    frame.pack(side="top", expand=True, fill="both")

    canv = myCanv(frame) #call the object in doGui.py


    menu = Menu(root)

    #the File meaubar
    fileBar = Menu(menu)
    fileBar.add_command(label="Open", command=lambda:canv.OpenFile())
    fileBar.add_command(label="Save", command=lambda:canv.SaveFile())
    fileBar.add_command(label="Save As", command=lambda:canv.SaveAsFile())
    menu.add_cascade(label='File', menu=fileBar)

    #undo meaubar
    menu.add_command(label="Undo", command=lambda:canv.undo())



    #the edit meaubar
    editBar = Menu(menu)

    cstBar = Menu(editBar)
    cstBar.add_command(label="linearly", command=lambda:canv.doLinear())
    cstBar.add_command(label="exponentially", command=lambda:canv.doExp())
    cstBar.add_command(label="logarithmically", command=lambda:canv.doLog())

    editBar.add_cascade(label='adjust contrast', menu=cstBar)
    editBar.add_command(label="resize", command=lambda:canv.resize())
    editBar.add_command(label="rotate", command=lambda:canv.rotate())
    editBar.add_command(label="gray-levl slicing", command=lambda:canv.sliceGrayLV())
    editBar.add_command(label="auto-level", command=lambda:canv.autolevl())
    editBar.add_command(label="bit-plane", command=lambda:canv.bit_plane())
    editBar.add_command(label="sharpen", command=lambda:canv.sharp())
    editBar.add_command(label="smooth", command=lambda:canv.smooth()) 
    menu.add_cascade(label='Edit', menu=editBar)

    

    root.config(menu=menu)

    root.mainloop()