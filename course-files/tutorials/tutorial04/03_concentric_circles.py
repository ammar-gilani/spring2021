from tkinter import Canvas, Tk
from helpers import make_circle

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


# TODO: Make concentric circles  using a while loop
make_circle(canvas, (100, 50), 25, color=None)




########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()