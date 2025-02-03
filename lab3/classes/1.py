class Upperr:
  def __init__(self):
    self.up=""

  def getString(self):
    self.up=input()

  def printString(self):
    print(self.up.upper())

a = Upperr()
a.getString()
a.printString()
 