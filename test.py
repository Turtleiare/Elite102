class Bank_Account:
  def __init__(self, bal):
    self.balance = bal
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self,amount):
    if self.balance >= amount:
      self.balance -= amount
    else:
      print('Insufficient funds')
  def get_bal(self):
    return self.balance
  def __str__(self):
    final_bal='The New Balance is $'+ format(self.balance,'.2f')
    return final_bal
def main():
  print('Welcome to the bank!')
  start_bal = float(input('Please enter your statrting balance $:'))
  checking = Bank_Account(start_bal)
  pay=float(input('How much are you trying to deposit? $: '))
  checking.deposit(pay)
  print('Your account balance is $:', format(checking.get_bal(),',.2f'))
  cash = float(input('How Much would you like to withdraw?: $'))
  checking.withdraw(cash)
  print(checking)
main()