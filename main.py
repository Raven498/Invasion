import tkinter as tk
class Earth:
  pass
class Mars:
  pass
class Jupiter:
  pass
class Saturn:
  pass
class Ship:
  pass
class Display:
  def __init__(self, window, canvas, planet_list, ship_list):
    self.window = window
    self.canvas = canvas
    self.planet_list = planet_list
    self.ship_list = ship_list

  def create(self):
    x1 = 10
    y1 = 10
    x2 = 100
    y2 = 100
    for i in range(2):
      for j in range(2):
        self.canvas.create_oval(x1, y1, x2, y2, fill='green')
        x1 = 610
        x2 = 700
      x1 = 10
      x2 = 100
      y1 = 410
      y2 = 500
      

window = tk.Tk()
canvas = tk.Canvas(window, width=700, height=700, bg="black")
canvas.pack()

earth = Earth()
mars = Mars()
jupiter = Jupiter()
saturn = Saturn()
planet_list = [earth, mars, jupiter, saturn]
ship_list = []

display = Display(window, canvas, planet_list, ship_list)
display.create()

window.mainloop()