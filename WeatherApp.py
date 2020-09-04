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
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

# button widget
button = tk.Button(root, text="Test Button", bg='blue')
button.pack()

# to run your application
root.mainloop()

"""

"""