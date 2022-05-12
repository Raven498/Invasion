import tkinter as tk
class Planet:
  def __init__(self, name):
    self.name = name
    if self.name == "Earth":
      self.earth_advantage = True
    elif self.name == "Mars":
      self.mars_advantage = True
    elif self.name == "Jupiter":
      self.jupiter_advantage = True
    elif self.name == "Saturn":
      self.saturn_advantage = True
    self.ship_list = []
    for i in range(8):
      ship = Ship(300, 50)
      self.ship_list.append(ship)
    

class Ship:
  def __init__(self, hp, dp):
    self.hp = hp
    self.dp = dp

class Display:
  def __init__(self, window, canvas, planet_list):
    self.window = window
    self.canvas = canvas
    self.planet_list = planet_list

  def create(self):
    x1 = 10
    y1 = 10
    x2 = 100
    y2 = 100
    planet_index = 0
    for i in range(2):
      for j in range(2):
        self.canvas.create_oval(x1, y1, x2, y2, fill='green')
        self.canvas.create_text(x1 + 45, y1 + 30, 
                                text=planet_list[planet_index].name, 
                                fill="black", 
                                font="Helvetica 15 bold")
        x_factor = 0
        y_factor = 90
        for ship in planet_list[planet_index].ship_list:
          size = int(canvas["width"])
          midpoint = size / 2
          if x1 + x_factor == midpoint + x1 or x1 + x_factor >= size :
            y_factor += 60
            x_factor = 0
          self.canvas.create_oval(x1 + x_factor, 
                                  y1 + y_factor, 
                                  x2 + (x_factor - 40), 
                                  y2 + (y_factor - 40),
                                  fill="red")
          x_factor += 100
        x1 = 610
        x2 = 700
        planet_index += 1
      x1 = 10
      x2 = 100
      y1 = 410
      y2 = 500
      

window = tk.Tk()
window.update()
canvas = tk.Canvas(window, width=1000, height=1000, bg="white")
canvas.pack()

earth = Planet("Earth")
mars = Planet("Mars")
jupiter = Planet("Jupiter")
saturn = Planet("Saturn")
planet_list = [earth, mars, jupiter, saturn]

display = Display(window, canvas, planet_list)
display.create()

window.mainloop()