class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0.0

  def __str__(self):
    header = self.name.center(30, "*")
    ledger = ""

    for entry in self.ledger:
      description = entry["description"][:23].ljust(23)
      amount = str(format(entry["amount"], ".2f"))[:7].rjust(7)
      ledger += f"{description}{amount}\n"

    return f"{header}\n{ledger}Total: {self.balance}"

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    status = self.check_funds(amount)

    if status == False:
      return status
    
    self.ledger.append({"amount": -amount, "description": description})
    self.balance -= amount
    return status

  def get_balance(self):
    return self.balance

  def transfer(self, amount, obj):
    status = self.check_funds(amount)
    if status == False:
      return status
    
    self.withdraw(amount, f"Transfer to {obj.name}")
    
    obj.deposit(amount, f"Transfer from {self.name}")
    return status

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

def create_spend_chart(categories):
  total = 0
  spent_amounts = {}
  spent_percentage = {}
  descriptions = []
  
  for category in categories:
      spent_amounts[category.name] = 0
      descriptions.append(category.name)
      
      for entry in category.ledger:
          if entry["amount"] < 0:
              total += abs(entry["amount"])
              spent_amounts[category.name] += abs(entry["amount"])
  
  for category in categories:
      spent_percentage[category.name] = round((spent_amounts[category.name] / total) * 100, -1)
      
  header = "Percentage spent by category"
  chart = ""
  
  for i in range(100, -10, -10):
      chart += f"{i}|".rjust(4)
      
      for _, percent in spent_percentage.items():
          if percent >= i:
              chart += " o "
          else:
              chart += "   "
    
      chart += " \n"

  footer = f"   {'-' * ((len(categories) * 3) + 1)}\n"
  
  max_desc_length = len(max(descriptions, key=len))
  for i in range(len(descriptions)):
      descriptions[i] = descriptions[i].ljust(max_desc_length)

  for line in zip(*descriptions):
      footer += "    " + "".join(map(lambda char: char.center(3), line)) + " \n"

  result = f"{header}\n{chart}{footer}"
  return result

obj = Category("Food")
obj2 = Category("Entertainment")
obj3 = Category("Business")
obj.deposit(900, "deposit")
obj2.deposit(900, "deposit")
obj3.deposit(900, "deposit")
obj.withdraw(105.55)
obj2.withdraw(33.40)
obj3.withdraw(10.99)
print(create_spend_chart([obj3, obj, obj2]))
