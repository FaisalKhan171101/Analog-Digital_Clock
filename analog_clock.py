import tkinter
import math
import time

canvas_size = 700
canvas = tkinter.Canvas(bg="#08141a", width=canvas_size, height=canvas_size)
canvas.pack()

radius = 250
angle = 270

elements = [0 for _ in range(5)]


def calculate(_angle, _radius):
    x = math.cos(math.radians(_angle)) * _radius + canvas_size / 2
    y = math.sin(math.radians(_angle)) * _radius + canvas_size / 2

    return x, y


def line(_x1, _y1, _x2, _y2, _width, _color):
    return canvas.create_line(_x1, _y1, _x2, _y2, width=_width, fill=_color, capstyle="round")


def line_from_center(_x, _y, _width, _color):
    return line(canvas_size / 2, canvas_size / 2, _x, _y, _width, _color)


def text(_x, _y, _text, _color):
    return canvas.create_text(_x, _y, text=_text, fill=_color, font=("PT Sans", 35, "bold"),
                              justify="center")


def draw(elements):
    for element in elements:
        canvas.delete(element)

    tm = time.localtime()

    # Digital time
    digital_time = time.strftime('%H:%M:%S\n%d.%m.%Y', tm)
    elements[0] = text(canvas_size / 2, canvas_size / 2 + 80, digital_time, "#b36b47")

    # Hour hand
    x, y = calculate((360 / 12) * tm[3] + (360 / 12 / 60) * tm[4] - 90, radius - 90)
    elements[1] = line_from_center(x, y, 12, "#8c2a4b")

    # Minute hand
    x, y = calculate((360 / 60) * tm[4] + (360 / 60 / 60) * tm[5] - 90, radius - 40)
    elements[2] = line_from_center(x, y, 7, "#2a8c7c")

    # Second hand
    x1, y1 = calculate((360 / 60) * tm[5] + 90, radius - 200)
    x2, y2 = calculate((360 / 60) * tm[5] - 90, radius - 30)
    elements[3] = line(x1, y1, x2, y2, 4, "#2a638c")

    # Small circle in center
    elements[4] = canvas.create_oval(canvas_size / 2 - 10, canvas_size / 2 - 10,
                                     canvas_size / 2 + 10, canvas_size / 2 + 10, fill="#405b80",
                                     width=0)

    return elements


for i in range(12):
    x, y = calculate(angle + 30, radius - 45)
    text(x, y, i + 1, "#478fb3")

    angle += 360 / 12

for i in range(60):
    if i % 5 == 0:
        x1, y1 = calculate(angle + 30, radius - 10)
        width = 5
    else:
        x1, y1 = calculate(angle + 30, radius)
        width = 3

    x2, y2 = calculate(angle + 30, radius + 10)
    line(x1, y1, x2, y2, width, "#334780")

    angle += 360 / 60

while True:
    elements = draw(elements)
    canvas.update()
