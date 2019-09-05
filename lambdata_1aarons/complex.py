class Complex:
    """Takes two numbers representing the real and imaginary 
    parts of a complex number."""
    # https://thepythonguru.com/python-operator-overloading/
    # https://www2.clarku.edu/faculty/djoyce/complex/mult.html
    # https://www2.clarku.edu/faculty/djoyce/complex/div.html

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    """Adds two complex numbers together."""

    def __add__(self, second):
        return self.r+second.r, self.i+second.i

    """Subtracts the second complex number from the first."""

    def __sub__(self, second):
        return self.r-second.r, self.i-second.r

    """Multiply first complex number by second."""

    def __mul__(self, second):
        real = self.r*second.r-self.i*second.i
        imaginary = self.r*second.i+self.i*second.r
        return real, imaginary

    """Divide first complex number by second."""

    def __truediv__(self, second):
        denominator = second.r*second.r+second.i*second.i
        real = (self.r*second.r+self.i*second.i)/denominator
        imaginary = (self.i*second.r-self.r*second.i)/denominator
        return real, imaginary
