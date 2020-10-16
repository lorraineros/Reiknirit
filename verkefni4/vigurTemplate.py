import math
class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):     
        print('[' + str(self.x) + ' ' + str(self.y) + ']')

    # Fall sem skilar lengd
    def lengd(self):        
        lengdV = round((self.x**2+self.y**2)**0.5, 2)
        return lengdV
    
    # Fall sem skilar hallatölu
    def halli(self):        
        halliV = round((self.y / self.x), 2)
        return halliV
    
    # Fall sem skilar þvervigri
    def thvervigur(self):
        Vigur.thver = Vigur((self.y * -1), self.x)
        return Vigur.thver
    
    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        stefh = round(math.degrees(math.atan(self.y / self.x)), 1)
        return stefh
    
    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        hornV = round(v.stefnuhorn() - self.stefnuhorn(), 2)
        return hornV
    
    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v): 
        Vigur.summa = Vigur(self.x + v.x, self.y + v.y)
        return Vigur.summa


# Keyrsluforrit
v1 = Vigur(1,3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vth = v1.thvervigur()
print("Þvervigur: " , end=" ")
vth.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())    
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()

