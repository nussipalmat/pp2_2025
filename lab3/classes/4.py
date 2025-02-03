class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def show(self):
      print(f"{self.x} {self.y}")
  def move(self,newx,newy):
      self.x=newx
      self.y=newy
  def dist(self, p):
      return ((p.x - self.x)** 2 + (p.y - self.y)** 2)**0.5
  
p1 = Point(2,3)
p2 = Point(5,4)

p1.show()
p2.show()

p1.move(7,8)

p1.show()

print(p1.dist(p2))