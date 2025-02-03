class Account:
  def __init__(self,owner="",balance=0):
    self.owner=owner
    self.balance=balance
  def withdraw(self,withd):
    if self.balance>=withd:
      self.balance-=withd
  def deposit(self,dep):
    self.balance+=dep

user=Account("Almat",1000)
user.deposit(5000)
print(user.balance)

user.withdraw(6000)
print(user.balance)

user.deposit(3000)
user.withdraw(4000)
print(user.balance)