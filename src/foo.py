

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

    #------------------------------------------------------
    # List 
    #   - ordered collection of items
    #   - items may be different
    def list(self):
        a = [1, 2, 3, 4];
        a.append(5)        # Append item
        a.append([1,2,3])  # Append item [1,2,3,4,[1,2,3]]
        a.extend([6,7,8])  # Extend list
        a.insert(1,42)     # Insert 42 at 1
        a.remove(42)       # Remove value of 42
        a.insert(0,0)      # Insert 0 at 0
        a.pop()            # Remove first item 0
        a.count(8)         # Counts 8s 
        a.sort()           # Sort  cmp, key, reverse
        a.reverse()        # Reverse the list
        return a

    #------------------------------------------------------
    # Tuples 
    #   - faster than lists 
    #   - immutable 
    #   - Used as dict keys
    def tuple(self):      
        a = (1, 2, 3, 4)
        a.index(2)         # Index of 3 is 3
        a.count(2)         # Count of the value 2 is 1
        b = a[1:3]         # Slicing
        str(b)             # Convert to string
        len(b)             # Length
        return b

    #------------------------------------------------------
    # Dict  
    #   - no duplicate keys 
    #   - no order
    def dict(self):
        a = { 'a':'str', 'b':[1,2] }
        a.keys()                      # Key list
        a.items()                     # Item list
        a.iteritems()                 # Iterator 
        a.has_key('first')            # Check existence
        'a' in a                  # Check existence
        a.get('b')                # Get Value
        a.pop('a')                # Get and remove item
        a.popitem()                   # Removes and returns a random item
        a.setdefault('a','')      # Create a new item
        a['a']                    # Get value
        b = a.copy()                  # Shallow copy
        #b = a.deepcopy()              # Deep copy
        b.clear()                     # Clear
        b = a.fromkeys(['a'])     # Create a new dict from key list
        b = {}.fromkeys(['a'])
        a = {'a':1}
        b = {'a':2, 'b':2}
        a.update(b)                 # Update sets a to 2 and appends b
        a.iteritems()                 # Item iterator
        a.iterkeys()                  # Key iterator
        a.itervalues()                # Value iterator
        a == b                        # Compare dicts
        return a


    #------------------------------------------------------
    # String  
    #   - immutable
    #   - 
    def string(self): 
        a = 'The string'              # Single quote
        b = "The string"              # Double quote
        c = '''The                    
               String'''              # Triple quote 
        d = """Special String ' " """ # Quotes in triple quotes
        a[0]                          # Character access
        a = a[4:]                     # Slice string
        "%s" % "some text"            # % formatting
        b = a + a                     # Concatenate
        c = a*3                       # Multiply
        '12'.isdigit()                # Digits only        
        'as'.isalpha()                # Alphabetic characters only
        '1a'.isalnum()                # Alphabetic characters and digits
        'AA'.isupper()                # Uppercase
        'aa'.islower()                # Lowercase
        'Ta'.istitle()                # Starts with capital
        '  '.isspace()                # Spaces only
        'aa'.count('a')               # Count occurences
        len('aa')                     # Length
        'aa'.title()                  # Capitalize first leter of each word
        'aa'.capitalize()             # Capitalize first leter
        'AA'.lower()                  # Lower case
        'aa'.upper()                  # Upper case
        'Aa'.swapcase()               # Swap case 
        b = a.center(40)              # Center in new string
        #c = a.just(40,'-')            # Right justify in new string
        c = a.zfill(40)               # Zero file right justify
        a.strip()                     # Remove left and right trailing space
        a.lstrip()                    # Remove left trailing space
        a.rstrip()                    # Remove right trailing space
        '\t'.expandtabs()             # Expand tabs


        return 0


    #------------------------------------------------------
    # Set  
    #   -  
    #   -   
    def set(self):
        return 0


    #------------------------------------------------------
    # FrozenSet  
    #   -  
    #   - 
    def frozenset(self): 
        return 0


#lists, tuples, dictionaries, strings, sets and frozensets


if __name__ == "__main__":
    fooBar = Foo()
    print fooBar.getFooBar()
    print fooBar.list()
    print fooBar.tuple()
    print fooBar.dict()
    print fooBar.string()
    print fooBar.set()
    print fooBar.frozenset()
    0