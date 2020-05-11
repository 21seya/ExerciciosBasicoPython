import pickle

class account:
    def __init__ (self, id, balance): 
        self.id = id
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount

myac=account('123',100) 
myac.deposit(800) 
myac.withdraw(500)

fd = open('archive','wb') 
pickle.dump(myac, fd) 
fd.close()

myac.deposit(200) 
print (myac.balance)

fd = open( 'archive', 'rb') 
myac = pickle.load(fd) 
fd.close()
