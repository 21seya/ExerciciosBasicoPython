class NumFactory:
    def init (self, n): 
        self.val = n
    def timesTwo(self): 
        self.val *= 2
    def plusTwo(self): 
        self.val += 2

f = NumFactory(2) 
for m in dir(f):
    mthd = getattr(f,m) 
if callable(mthd):
    mthd()
