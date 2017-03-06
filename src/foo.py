

class Foo(object): 

    def __init__(self):

        object.__init__(self)
        print 'Constructing Foo'
        self.foo_bar = 0
        self.__bar(42)
      
    def getFooBar(self):
        print 'Get the Foo Bar'
        return self.foo_bar

    def __bar(self, num):

        print 'Private Bar Function'
        self.foo_bar = num


if __name__ == "__main__":
    fooBar = Foo()
    print str(fooBar.getFooBar())