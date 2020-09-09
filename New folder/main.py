import tkinter
from tkinter import messagebox
from PIL import ImageGrab
import png_to_number
import sys

sys.path.append('webcolors-1.11.1/src')
sys.path.append('PyAutoGUI-0.9.50')

import webcolors
import pyautogui


last_x, last_y = 0, 0
action_list = list()
color_selected = 1


def xy(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


def add_line(event):
    global last_x, last_y, action_list
    action_list.append(canvas.create_line(last_x, last_y, event.x, event.y, width=20, fill=color(num=color_selected)))
    last_x, last_y = event.x, event.y


def save(event):
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    im = ImageGrab.grab((x, y, x1, y1))
    im.save('canvas.png')
    num = png_to_number.run_example()
    messagebox.showinfo('Results', f'Your number is: {num}')


def delete(event):
    canvas.delete('all')


def undo(event):
    global action_list
    try:
        canvas.delete(action_list[-1])
        action_list.pop(-1)
    except IndexError:
        pass


def color(event=None, num=0):
    global color_selected
    color_list = {'1': 'white', '2': 'brown', '3': 'yellow', '4': 'red', '5': 'orange',
                  '6': 'pink', '7': 'gray', '8': 'purple', '9': 'blue', '0': 'green'}
    color_selected = num
    return color_list[str(num)]


def detect(event):
    x_y = tuple(pyautogui.position())
    x_y = tuple(pyautogui.position())
    c = webcolors.rgb_to_name((ImageGrab.grab().load()[x_y[0], x_y[1]]))
    messagebox.showinfo('Color', f'The Color Selected: {c}')


# if __name__ == '__main__':
root = tkinter.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

canvas = tkinter.Canvas(root, bg='black', height=500, width=500)
canvas.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
canvas.bind('<Button-1>', xy)
canvas.bind('<B1-Motion>', add_line)
root.bind('<Control-s>', save)
root.bind('<Control-d>', delete)
root.bind('<Control-z>', undo)
for i in range(10):
    def make_lambda(x):
        return lambda send: color(send, x)
    root.bind(f'{i}', make_lambda(i))
root.bind('<Button-3>', detect)

root.mainloop()
