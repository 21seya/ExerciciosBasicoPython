class A(object):
    @staticmethod
    def method(*argv):
        return argv

a = A()

print("a.method([1,2,3,4])=",a.method([1,2,3,4]))
print("Sem o @staticmethod")

        