class Category:
  def __init__(self,description):
    self.ledger = []
    self.description = description
    self.amount = 0.00
    self.tot_deposit = 0.00

  def __repr__(self):
      self.total = 0
      output = self.description.center(30, "*") + "\n"
      for item in self.ledger:
          output += item['description'].ljust(23)[:23]
          output += "{:.2f}".format(item['amount']).rjust(7)
          output += '\n'
    
      output += (f"Total: {str(self.amount)}")
      return output

  def check_funds(self,amount):
      if self.amount < amount:
          return False
      else:
          return True
  
  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description':description})
    self.amount += amount
    self.tot_deposit += amount

  def withdraw(self,amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount':-amount, 'description':description})
      self.amount -= amount
      return True
    else:
        return False

  def get_balance(self):
    return self.amount

  def transfer(self, amount, instance):
    if self.check_funds(amount):
      self.withdraw(amount,'Transfer to ' + instance.description)
      instance.deposit(amount,'Transfer from ' + self.description)
      return True
    else:
      return False

def create_spend_chart (categories):
  print('Percentage spent by category')
  for i in range(100,-1,-10):
    print((f"{i}| ").rjust(4),end="")
    for j in categories:
      percent =int(((j.tot_deposit - j.amount)*100)/j.tot_deposit)
      percent = (int(str(percent)[:1]))
      if (percent*10) >= i:
        print('o  ',end="")
    print('\n')
  print('    '+'-'*(3*len(categories)+1))

  for letter in range (10):
    print('    ',end="")
    for j in categories:
      if j.description[i] != None:
        print(f"{j.description[i]}   ",end="")
    print('\n')


  


  return''
