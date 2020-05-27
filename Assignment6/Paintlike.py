# making a paint like application using tk gui

from tkinter import * # we import everything from tkinter module
from tkinter import ttk, colorchooser, filedialog #filedialog for saving the file
import PIL #for image processing
from PIL import ImageGrab


class main():
    def __init__(self, master): #the constructer
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 1
        self.drawingTools()
        self.canvas.bind('<B1-Motion>',self.paint)
        self.canvas.bind('<ButtonRelease-1>',self.reset)

    def paint(self, new):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, new.x, new.y, 
            	width=self.penwidth, fill=self.color_fg, 
            	capstyle=ROUND,smooth=True)
                #create_line
        self.old_x = new.x
        self.old_y = new.y

    def reset(self, new):
        self.old_x = None
        self.old_y = None      

    def changeWidth(self, new):
        self.penwidth = new

    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics', '*.png')])
        if file:
            x = self.master.winfo_rootx() + self.canvas.winfo_x()
            y = self.master.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            PIL.ImageGrab.grab().crop((x, y, x1, y1)).save(file + '.png')
            
           

    def clear(self):
        self.canvas.delete(ALL)

    def change_fg(self):
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.canvas['bg'] = self.color_bg

    def drawingTools(self):
        self.controls = Frame(self.master, padx = 5, pady = 5)
        Label(self.controls, text='Pen Width: ',font=('',15)).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls, from_= 1, to = 75, command=self.changeWidth, orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=50)
        self.controls.pack()
        
        #creating a canvas for background
        self.canvas = Canvas(self.master, width=700, height=500, bg=self.color_bg)
        self.canvas.pack(fill=BOTH, expand=True)

        #creating menus
        menu = Menu(self.master)
        self.master.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Save As', command=self.save)

        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Pen Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)

        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear All', command=self.clear)
        optionmenu.add_command(label='Quit Paint_Like_App', command=self.master.destroy) 
        
        

if __name__ == '__main__':
    run = Tk()
    main(run)
    run.title('Paint_Like_App')
    run.mainloop()
