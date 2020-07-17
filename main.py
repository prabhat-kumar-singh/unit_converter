from tkinter import *

window = Tk()
window.title("Unit Converter")

large_font = ('Verdana',30)
#A drop down to select the units to work with
units = StringVar()
units.set("length")
unit_message = Label(text = "Select Unit")
unit_message.grid(row = 0, column = 1)
units_menu = OptionMenu(window, units, "length", "mass", "temperature", "speed", "time")
units_menu.grid(row = 1, column = 0, columnspan = 3)

#Getting user Input
first_unit = Entry(width = 10, borderwidth = 5, font = large_font)
first_unit.grid(row = 2, column = 0)
equal = Label(text = "=")
equal.grid(row = 2, column = 1)
v = StringVar()
v.set("0")
second_unit = Label(window, textvariable = v, bg = "white", width = 10, height = 3)
second_unit.grid(row = 2, column = 2)

#Drop down to select units
first_unit_val = StringVar()
first_unit_val.set("metre")
first_unit_container = OptionMenu(window, first_unit_val, 'kilometre', 'metre', 'centimetre', 'millimetre', 'micrometre', 'nanometre', 'mile')
first_unit_container.grid(row = 3, column = 0)

second_unit_val = StringVar()
second_unit_val.set("centimetre")
second_unit_container = OptionMenu(window, second_unit_val, 'kilometre', 'metre', 'centimetre', 'millimetre', 'micrometre', 'nanometre', 'mile')
second_unit_container.grid(row = 3, column = 2)




window.mainloop()