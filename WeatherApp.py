import tkinter as tk

# defining height and width for the arguments (const)
HEIGHT = 700
WIDTH = 800

# root window
root = tk.Tk()

# placeholder to get initial screen size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# to start organizing the widgets you put on screen
frame = tk.Frame(root, bg='#e6e6e6')
#relwidth and relheight work as percentage of a screen
frame.place(relwidth = 0.8, relheight = 0.5, relx = 0.1, rely = 0.1)

# button widget
button = tk.Button(frame, text="Get Weather", bg='blue')
button.place(relx=0, rely=0, relwidth=0.2, relheight=0.1)

# this is a label
# label = tk.Label(frame, text="This is a label", bg='yellow')
# label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

# # something you can type in (form)
# entry = tk.Entry(frame, text="This is an entry", bg='gray')
# entry.place(relx=0.8, rely=0, relwidth = 0.8, relheight = 0.25)

# to run your application
root.mainloop()

"""
you can use place(), grid(),pack()
relwidth = how wide you want that item (x axis (left to right))
relheight = how tall you want that item (y axis (up and down))
relx = what percent of x axis you want to start at
rely = what percentage of y you want to start at

"""