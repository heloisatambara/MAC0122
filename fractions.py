def MCD(n1, n2): # function to find the maximum common divider - will be used to simplify fractions.
    rest = n1 % n2
    while rest != 0:
        n1 = n2
        n2 = rest
        rest = n1 % n2
    return n2
    
class fraction: # creates the class

# operations
    def __init__(self, numerator=0, denominator=1): # define instances
        self.num = numerator
        self.den = denominator
        if denominator == 0:
            raise ValueError('Denominator can't be 0.')
        
        if denominator < 0:
            self.num = -numerator
            self.den = -denominator
            
    def __add__(self, frac2): # sum operation
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        dencom = self.den * frac2.den
        num1 = self.num * frac2.den
        num2 = frac2.num * self.den
        return fraction(num1 + num2, dencom)
        
    def __sub__(self, frac2): # subtraction operation
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        dencom = self.den * frac2.den
        num1 = self.num * frac2.den
        num2 = frac2.num * self.den
        return fraction(num1 - num2, dencom)
    
    def __mul__(self, frac2): # multiply operation
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        deno = self.den * frac2.den
        nume = self.num * frac2.num
        return fraction(nume, deno)
        
    def __truediv__(self, frac2): # division operation (with '/') 
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        fr2 = fraction(frac2.den, frac2.num)
        return self * fr2
        
    def __pow__(self, exp): # power operation
        if type(exp) == fraction:
            exp = exp.num / exp.den
        if exp >= 0:
            nume = self.num ** exp
            deno = self.den ** exp
        if exp <= 0:
            exp = -exp
            nume = self.den ** exp
            deno = self.num ** exp
        return fraction(nume, deno)
 #

 # comparisons
    def __eq__(self, frac2): # equal to
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        elif type(frac2) != fraction:
            return False
        fac1 = self.num * frac2.den
        fac2 = self.den * frac2.num
        return fac1 == fac2
    
    def __ne__(self, frac2): # not equal to
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        elif type(frac2) != fraction:
            return True
        fac1 = self.num * frac2.den
        fac2 = self.den * frac2.num
        return fac1 != fac2
                
    def __lt__(self, frac2): # less than
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        f1 = self.num / self.den
        f2 = frac2.num / frac2.den
        return f1 < f2
        
    def __le__(self, frac2): # less or equal 
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        f1 = self.num / self.den
        f2 = frac2.num / frac2.den
        return f1 <= f2
        
    def __gt__(self, frac2): # greater than
        if type(frac2) == int or type(frac2) == float:
            frac2 = fraction(frac2)
        f1 = self.num / self.den
        f2 = frac2.num / frac2.den
        return f1 > f2
        
    def __ge__(self, frac2): # greater or equal
        if type(frac2) == int or type(frac2) == float:
            fraction(frac2)
        f1 = self.num / self.den
        f2 = frac2.num / frac2.den
        return f1 >= f2
 #


    def __str__(self): # how print shows the fraction
        maxdiv = MCD(self.num, self.den)
        self.num = self.num // maxdiv
        self.den = self.den // maxdiv
    
        if self.den == 1:
            return str(int(self.num))
        else:
            return str(int(self.num)) + '/' + str(int(self.den))


 # run tests
if __name__ == "__main__":
    
   x = fraction(-2, -8)
   y = fraction(1, -2)
   z = x + y
   print(z)
   print(x < y or x < z)
   print(y - z * x)
   print(x ** 3)
   print(x * y + z)
