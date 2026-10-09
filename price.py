import math
class Price:
    def __init__(self, base, time):
        self.base= base
        self.time= time
    def price_equation(self):
        return self.base*(1+(((-0.557)*math.sin(((-48.264)*self.time)))+((self.time-0.231)*self.time*self.time)))
    

