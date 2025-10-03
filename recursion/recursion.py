class recursion:
    def number(self, n):
        if n == 0:
            return 0
        self.number(n-1)
        print(n)
    def reverserNumber(self, n):
        if n == 0:
            return 0
        print(n)
        self.reverserNumber(n-1)
    def odd(self, n):
        if n == 0:
            return 0
        self.odd(n-1)
        if n % 2 != 0:
            print(n)
    def even(self, n):
        if n == 0:
            return 0
        self.even(n-1)
        if n % 2 == 0:
            print(n)
    

#driver code
r= recursion()
# r.number(5)
# r.reverserNumber(5)
r.odd(5)