from tkinter import *
import json

window = Tk()
window.title("Unit Converter")

large_font = ('Verdana',30)

first_unit_val, second_unit_val = StringVar(), StringVar()

unit_drop_down_list = [
    ("first", 'length', 'metre', OptionMenu(window, first_unit_val, 'kilometre', 'metre', 'centimetre', 'millimetre', 'micrometre', 'nanometre', 'mile')), 
    ("first", 'mass', 'gram', OptionMenu(window, first_unit_val, 'tonne', 'kilogram', 'gram', 'milligram', 'pound')), 
    ("first", "temperature", 'celsius', OptionMenu(window, first_unit_val, 'celsius', 'fahrenheit', 'kelvin')), 
    ("first", 'time', 'minute', OptionMenu(window, first_unit_val, 'nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day')),
    ("second", 'length', 'centimetre', OptionMenu(window, second_unit_val, 'kilometre', 'metre', 'centimetre', 'millimetre', 'micrometre', 'nanometre', 'mile')), 
    ("second", 'mass', 'milligram', OptionMenu(window, second_unit_val, 'tonne', 'kilogram', 'gram', 'milligram', 'pound')), 
    ("second", "temperature", 'fahreinheit', OptionMenu(window, second_unit_val, 'celsius', 'fahrenheit', 'kelvin')), 
    ("second", 'time', 'second', OptionMenu(window, second_unit_val, 'nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'))
    ]


#Drop down to select units
def unit_dropdown(unit):
    for o, u, f, i in unit_drop_down_list:
        if u == unit and o == "first":
            first_unit_val.set(f)
            first_unit_container = i
            first_unit_container.grid(row = 3, column = 0)
    for o1, u1, f1, i1 in unit_drop_down_list:
        if u1 == unit and o1 == "second":
            second_unit_val.set(f1)
            second_unit_container = i1
            second_unit_container.grid(row = 3, column = 2)

#Function for length unit
def length(first, second):
    global first_unit, second_unit, v, res
    with open("units.json", "r") as f:
        res = json.load(f)
        res = res['units']['length']
    get_value = res[first][second]
    ans = float(first_unit.get()) * float(get_value)
    v.set(str(ans))

def mass(first, second):
    global first_unit, second_unit, v, res
    with open("units.json", "r") as f:
        res = json.load(f)
        res = res['units']['mass']
    get_value =  res[first][second]
    ans = float(first_unit.get()) * float(get_value)
    v.set(str(ans))

def temperature(first, second):
       global first_unit, second_unit, v, res
       ans = 0
       if first == "celsius" and second == "fahrenheit":
           C = float(first_unit.get())
           F = (C * 9/5) + 32
           ans = F
       elif first == "celsius" and second == "kelvin":
            C = float(first_unit.get())
            K = C + 273.15
            ans = K
       elif first == "celsius" and second == "celsius":
            ans = 1
       elif first == "fahrenheit" and second == "celsius":
            F = float(first_unit.get())
            C = (F - 32) * 5/9
            ans = C
       elif first == "fahrenheit" and second == "kelvin":
            F = float(first_unit.get())
            K = (F - 32) * 5/9 + 273.15
            ans = K
       elif first == "fahrenheit" and second == "fahrenheit":
            ans = 1
       elif first == "kelvin" and second == "celsius":
            K = float(first_unit.get())
            C = K - 273.15
            ans = C
       elif first == "kelvin" and second == "fahrenheit":
            K = float(first_unit.get())
            F = ((K - 273.15) * 9/5) + 32
       elif first == "kelvin" and second == "kelvin":
            ans = 1
       v.set(str(ans))


def unit_conversion(unit, first, second):
    if unit == "length":
        length(first, second)
    elif unit == "mass":
        mass(first, second)
    elif unit == "temperature":
        temperature(first, second)

#A drop down to select the units to work with
units = StringVar()
units.set("length")
unit_message = Label(text = "Select Unit")
unit_message.grid(row = 0, column = 1)
units_menu = OptionMenu(window, units, "length", "mass", "temperature", "time")
units_menu.grid(row = 1, column = 0, columnspan = 3)

#Getting user Input
first_unit = Entry(width = 10, borderwidth = 5, font = large_font)
first_unit.grid(row = 2, column = 0)
equal = Label(text = "=")
equal.grid(row = 2, column = 1)
v = StringVar()
v.set("0")
second_unit = Label(window, textvariable = v, bg = "white", width = 20, height = 3)
second_unit.grid(row = 2, column = 2)

#calling function
unit_dropdown(units.get())
btn = Button(window, text = "OK", command = lambda: unit_dropdown(units.get()))
btn.grid(row = 1, column = 1)

btn = Button(window, text = "CLICK HERE", command = lambda: unit_conversion(units.get(),first_unit_val.get(), second_unit_val.get()))
btn.grid(row = 4, column = 1)

window.mainloop()