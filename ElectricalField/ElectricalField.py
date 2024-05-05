class EField():
    # electricCharge = q, ε0 = 8.854 x 10-12, k, area = A, voltage = V , distance = d, force = F
    def __init__(self, electricCharge = 1, k =1, area = 1, voltage =1, distance =1, force =1):
        self.k = k
        self.area = area
        self.voltage = voltage
        self.distance = distance
        self.force = force
        self.electricCharge = electricCharge

    def eField_capacitor_1(self, electricCharge, k, area):
        ε0 = 8.854 * (10**12)
        return (round(electricCharge / (k*ε0*area), 2))
    
    def eField_capacitor_2(self, voltage, distance):
        return (round((voltage / distance), 2))
    
    def eField_inGeneral(self, k, electricCharge, distance):
        return ( round(((k * abs(electricCharge)) / (distance**2)), 2) )
    
    def eField_intensity(self, force, distance):
        return (round((force / distance), 2))