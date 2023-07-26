class Rectangle:
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def set_height(self, h):
    self.height = h

  def set_width(self, w):
    self.width = w

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    rect_str = ""

    for i in range(self.height):
      for i in range(self.width):
        rect_str += "*"
        if i == self.width - 1:
          rect_str += "\n"

    return rect_str

  def get_amount_inside(self, shape):
    return int(self.get_area() // shape.get_area())

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def set_side(self, side):
    self.set_height(side)
    self.set_width(side)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  

  
