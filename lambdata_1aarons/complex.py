class Complex:
    """Takes two numbers representing the real and imaginary 
    parts of a complex number."""
    # https://thepythonguru.com/python-operator-overloading/
    # https://www2.clarku.edu/faculty/djoyce/complex/mult.html
    # https://www2.clarku.edu/faculty/djoyce/complex/div.html

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __add__(self, second):
        """Adds two complex numbers together."""
        return self.r+second.r, self.i+second.i

    def __sub__(self, second):
        """Subtracts the second complex number from the first."""
        return self.r-second.r, self.i-second.i

    def __mul__(self, second):
        """Multiply first complex number by second."""
        real = self.r*second.r-self.i*second.i
        imaginary = self.r*second.i+self.i*second.r
        return real, imaginary

    def __truediv__(self, second):
        """Divide first complex number by second."""
        denominator = second.r*second.r+second.i*second.i
        real = (self.r*second.r+self.i*second.i)/denominator
        imaginary = (self.i*second.r-self.r*second.i)/denominator
        return real, imaginary
